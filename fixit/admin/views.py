from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from .serializer import  AdminLoginSerializer, AdminModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Admin

class AdminRegister(APIView):
    def post(self, request):
        serializer = AdminModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginUser(APIView):
    def post(self, request, format=None):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            userEmail = request.data.get('email')
            userPassword = request.data.get('password')
        
            try:

                user = Admin.objects.get(email = userEmail, password =userPassword)
            except:
                user = None

            if user:
                refresh = RefreshToken.for_user(user=user)
                refresh['admin']
                access_token = str(refresh.access_token)
                response= Response({'msg':'Login Successful','token':access_token, 'role':'admin'}, status=status.HTTP_200_OK)
                response.set_cookie(key='token', value=access_token, secure=True, httponly=True, samesite="None")
                return response
            else:
                return Response({'msg':'Invalid Id or password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


