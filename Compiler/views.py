from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import requests
import os
from django.http import HttpResponse
from django.conf import settings
# from django.contrib.auth.decorators import user_passes_test
import json
from .models import Codes
# Create your views here.
RUN_URL = u'https://api.hackerearth.com/v3/code/run/'


# User Registration
def Registration(request):
    if request.method == 'POST':
        email = request.POST['register_email']
        password = request.POST['register_pass']
        cnfrm_pass = request.POST['register_pass_cnrfm']
        first_name = request.POST['first_name']
        if cnfrm_pass == password:
            try:
                user = User.objects.get(username=email, password=password)
                messages.success(request, "User Already Exist, Please Login")
                return redirect('/login')
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=email,
                    password=cnfrm_pass,
                    first_name=first_name
                )
                user.save()
                user_4log = authenticate(request, username=email, password=cnfrm_pass)
                login(request, user_4log)
                return redirect('/')
        else:
            messages.success(request, "Password & Confirm Password won't Match...")
            return redirect('login')
    else:
        return render(request, 'Compiler/login_content.html')


# User Login
def Login(request):
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_pass']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "User won't Exist, Please sign up")
            return redirect('login')
    return render(request, 'Compiler/login_content.html')


# User Logout
def Logout(request):
    logout(request)
    messages.success(request, 'Logged out ! Successfully')
    return redirect('login')


# Default HomeView
def HomeView(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, 'Compiler/code_editor.html')
    else:
        return render(request, 'Compiler/login_content.html')


# Output of Your Code
def result(request):
    # print(request)
    if request.method == 'POST':
        api_key = "a5155987820558c556aaffa3c7ff3d771e4a0ed7"
        source = request.POST['source']
        language = request.POST['lang']
        testcases = request.POST['testcases']
        data = {
            'client_secret': api_key,
            'async': 0,
            'source': source,
            'lang': language,
            'time_limit': 5,
            'memory_limit': 262144,
            'input': testcases
        }

        r = requests.post(RUN_URL, data=data)
        # print(r.json())
        output = r.json()
        dic = {}
        if output['run_status']['status_detail'] == "NA":
            dic['output'] = output['run_status']['output_html']
            dic['compile_status'] = output['compile_status']
            return JsonResponse(dic)
        else:
            dic['output'] = output['run_status']['status_detail']
            dic['compile_status'] = output['compile_status']
            return JsonResponse(dic)


def fileSave(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        source = request.POST['source']
        extension = filename.split('.')
        if len(extension) != 2:
            return JsonResponse({"success": "Please Provide File Extension"})
        """directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(directory+'/media/files/'+filename, 'w+') as file:
            file.write(source)
            # file.name"""
        return JsonResponse({"success": 'success'})


def savedFiles(request):
    file_ = Codes.objects.filter(user_id=request.user.id)
    # print(file_)
    context = {
        "files": file_
    }
    return render(request, 'Compiler/FilesView.html', context)


def displayCode(request, id):
    codes = Codes.objects.filter(id=id)
    ex = codes.values()
    context = {
        "codes": codes
    }
    # print(context)
    return render(request, 'Compiler/view.html', context)

