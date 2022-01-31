from django.db import models

# Create your models here.
class Citizens (models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
class Feedback (models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50) 
    complain=models.CharField(max_length=1000)
class Request (models.Model):
     email=models.EmailField(max_length=50) 
     citizenaddress=models.CharField(max_length=200)  
     typeofwaste=models.CharField(max_length=30)   
   