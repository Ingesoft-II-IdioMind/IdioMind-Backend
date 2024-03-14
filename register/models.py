from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mail = models.EmailField(max_length = 45, unique=True)
    password = models.CharField(max_length = 45)
    names = models.CharField(max_length = 45)
    lastnames = models.CharField(max_length = 45)
    registerDate = models.DateField(default = timezone.now)
 
 


