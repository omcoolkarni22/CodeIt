from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name='HomeView'),
    path('result', result, name='result'),
    path('register', Registration, name='register'),
    path('login', Login, name='login'),
    path('logout', Logout, name='logout'),
    # path('fileSave', fileSave, name='fileSave'),
    # path('savedCodes', savedFiles, name='savedCodes'),
    # path('display/<int:id>', displayCode, name='displayCode')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

