from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Codes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # files = models.FileField(upload_to='files/', null=True, verbose_name="")
    content = models.TextField()
    filename_f = models.CharField(max_length=50, null=True, default='FileName')

    def get_absolute_url(self):
        return reverse("displayCode", kwargs={"id": self.id})         # f'/{ self.id }'
