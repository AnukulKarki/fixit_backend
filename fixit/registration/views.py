from django.shortcuts import render
from rest_framework.generics import CreateAPIView 
from .serializer import UserModelSerializer, WorkerModelSerializer
# Create your views here.

class RegistrationUser(CreateAPIView):
    serializer_class = UserModelSerializer

class RegistrationWorker(CreateAPIView):
    serializer_class = WorkerModelSerializer