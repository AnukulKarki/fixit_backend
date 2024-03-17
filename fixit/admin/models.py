from django.db import models

# Create your models here.

class Admin(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField( max_length=254, unique = True)
    password = models.CharField(max_length = 255)
    