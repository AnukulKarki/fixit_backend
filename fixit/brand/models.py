from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField( max_length=50)
    image = models.ImageField( upload_to='image/brand', null = True)

class BrandItem(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name = 'branditem')
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/branditem', null=True)