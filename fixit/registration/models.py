from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField( max_length=50)
    email = models.EmailField(max_length=50, unique = True)
    password = models.CharField( max_length=50)
    isKycVerified = models.BooleanField(default = False)
    phone = models.CharField(max_length=50)

class userProfile(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    age = models.IntegerField()
    district = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    street_name = models.CharField( max_length=50)
    image = models.ImageField(upload_to=None, null=True)
    rating = models.IntegerField()
    citizenship_np = models.CharField( max_length=50, null = True)
    
    


class Worker(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField( max_length=50)
    email = models.EmailField(max_length=50, unique = True)
    password = models.CharField( max_length=50)
    isKycVerified = models.BooleanField(default = False)
    phone = models.CharField(max_length=50)

class WorkerProfile(models.Model):
    worker = models.OneToOneField(Worker, on_delete = models.CASCADE, null = True)
    age = models.IntegerField()
    district = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    street_name = models.CharField( max_length=50)
    image = models.ImageField(upload_to=None, null=True)
    rating = models.IntegerField()
    citizenship_np = models.CharField( max_length=50, null = True)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

