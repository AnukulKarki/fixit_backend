from rest_framework import serializers
from .models import Brand, BrandItem


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandItem
        fields = '__all__'