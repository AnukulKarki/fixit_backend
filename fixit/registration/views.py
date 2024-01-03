from django.shortcuts import render
from rest_framework.generics import CreateAPIView 
from .serializer import UserModelSerializer
# Create your views here.

class RegistrationUser(CreateAPIView):
    serializer_class = UserModelSerializer