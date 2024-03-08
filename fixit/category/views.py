from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from .serializer import  CategoryModelSerializer
from .models import Category
# Create your views here.

class CategoryListView(APIView):
    def get(self, request):
        categoryObj = Category.objects.all()
        serializer = CategoryModelSerializer(categoryObj, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)