from rest_framework import serializers
from .models import Admin

class AdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 100)
    class Meta:
        model = Admin
        fields = ['email', 'password']

class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'