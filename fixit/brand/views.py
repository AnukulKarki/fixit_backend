from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import BrandItemModelSerializer, BrandModelSerializer
from .models import Brand, BrandItem


# Create your views here.


class BrandPostView(APIView):
    def post(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "admin":
                serializer = BrandModelSerializer(data = request.data)
                if serializer.is_valid():
                    title = serializer.data.get("title")
                    image = serializer.data.get("image")
                    Brand.objects.create(title = title, image = image)
                    return Response({'msg':'Brand Added Successfully'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'msg':'Only Valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)           

        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class BrandItemPostView(APIView):
    def post(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "admin":
                serializer = BrandItemModelSerializer(data = request.data)
                if serializer.is_valid():
                    brand = serializer.data.get("brand")
                    name = serializer.data.get("name")
                    price = serializer.data.get("price")
                    image = serializer.data.get("image")
                    BrandItem.objects.create(brand_id = brand, name = name, price = price,image = image)
                    return Response({'msg':'Brand Added Successfully'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'msg':'Only Valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)           

        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)