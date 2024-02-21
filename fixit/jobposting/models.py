from django.db import models
from registration.models import User, Category, Worker

# Create your models here.
class JobRequirement(models.Model):
    title = models.CharField( max_length=255)
    description = models.TextField()
    budget = models.IntegerField()
    isFeatured = models.BooleanField()
    latitude = models.TextField()
    longitude = models.TextField()
    location = models.TextField()
    image = models.ImageField(null= True)
    category =  models.ForeignKey(Category, on_delete = models.CASCADE , related_name = 'category')
    user = models.ForeignKey(User,on_delete = models.CASCADE,  related_name = 'user' )


class JobApply(models.Model):
    job = models.ForeignKey(JobRequirement, on_delete = models.CASCADE , related_name = 'job')
    worker = models.ForeignKey(Worker, on_delete = models.CASCADE , related_name = 'worker')
    status = models.CharField(max_length = 30)

class Job(models.Model):
    pass






