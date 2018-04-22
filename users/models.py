from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=50,blank=True)
    headshot = models.ImageField(upload_to='avator/%Y/%m/%d',default='default.jpg')
    signature = models.CharField(max_length=128,default='this guy is too lazy to leave anything here!')

    class Meta(AbstractUser.Meta):
        pass

