from django.db import models
from category.models import Category

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
    image = models.ImageField(upload_to=None, null=True)
    rating = models.IntegerField(default = 0)
    citizenship_no = models.CharField( max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=15, default = 'client')

