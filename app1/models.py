from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_pic=models.ImageField()
    address=models.TextField()

