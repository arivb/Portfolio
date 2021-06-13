from django.db import models
 
# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phonenumber=models.IntegerField()

class SignUp(models.Model):
    name=models.CharField(max_length=20)
    facebookid=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    age=models.CharField(max_length=10)
    