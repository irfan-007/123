from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_details(models.Model):
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)