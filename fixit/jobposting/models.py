from django.db import models
from registration.models import User
from category.models import Category
from django.utils import timezone

# Create your models here.
class JobRequirement(models.Model):
    title = models.CharField( max_length=255)
    description = models.TextField()
    budget = models.IntegerField()
    isFeatured = models.BooleanField(default = False)
    latitude = models.TextField()
    longitude = models.TextField()
    location = models.TextField()
    image = models.ImageField(null= True, upload_to='image/jobreq')
    category =  models.ForeignKey(Category, on_delete = models.CASCADE , related_name = 'jobreqcategory')
    user = models.ForeignKey(User,on_delete = models.CASCADE,  related_name = 'jobrequser' )
    jobStatus = models.CharField(max_length=50, default = "inprogress")
    created_at = models.DateTimeField(default=timezone.now)









