from django.db import models

#from django.contrib.auth.models import User 아래 처럼 쓰는 것이 맞다.
from django.conf import settings



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #이렇게 저용해 주세요
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
