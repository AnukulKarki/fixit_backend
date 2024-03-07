from django.db import models
from registration.models import User
from category.models import Category

# Create your models here.
class gig(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    worker = models.ForeignKey(User, on_delete = models.CASCADE , related_name = 'worker')
    category = models.ForeignKey(Category, on_delete = models.CASCADE , related_name = 'category')
    image = models.ImageField( upload_to=None, null=True)