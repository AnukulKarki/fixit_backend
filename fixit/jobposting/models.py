from django.db import models
from registration.models import User,  Worker
from category.models import Category
from django.utils import timezone

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
    category =  models.ForeignKey(Category, on_delete = models.CASCADE , related_name = 'jobreq_category')
    user = models.ForeignKey(User,on_delete = models.CASCADE,  related_name = 'jobreq_user' )
    jobStatus = models.CharField(max_length=50, default = "inprogress")
    created_at = models.DateTimeField(default=timezone.now)









