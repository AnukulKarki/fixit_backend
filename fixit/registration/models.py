from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField( max_length=50)
    email = models.EmailField(max_length=50, unique = True)
    password = models.CharField( max_length=50)
    isKycVerified = models.BooleanField(default = False)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()
    district = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    street_name = models.CharField( max_length=50)
    image = models.ImageField(upload_to=None)
    rating = models.IntegerField(default = 0)
    citizenship_no = models.CharField( max_length=50)
    
    


class Worker(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField( max_length=50)
    email = models.EmailField(max_length=50, unique = True)
    password = models.CharField( max_length=50)
    isKycVerified = models.BooleanField(default = False)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()
    district = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    street_name = models.CharField( max_length=50)
    image = models.ImageField(upload_to=None)
    rating = models.IntegerField(default = 0)
    citizenship_no = models.CharField( max_length=50)
    


