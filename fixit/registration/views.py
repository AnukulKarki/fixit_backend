from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializer import UserModelSerializer, WorkerModelSerializer, WorkerLoginSerializer, UserLoginSerializer
from .models import Worker, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import verify_access_token 
# Create your views here.

class RegistrationUser(CreateAPIView):
    serializer_class = UserModelSerializer

class RegistrationWorker(CreateAPIView):
    serializer_class = WorkerModelSerializer


class loginUser(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            userEmail = request.data.get('email')
            userPassword = request.data.get('password')
        
            try:

                user = User.objects.get(email = userEmail, password =userPassword)
            except:
                user = None

            if user:
                # refresh = RefreshToken.for_user(user={"id":user["email"],"role":"user"})  # replace 'user' with the authenticated user
                refresh = RefreshToken.for_user(user=user)
                refresh["role"]="user"
                access_token = str(refresh.access_token)
                response= Response({'msg':'Login Successful','token':access_token}, status=status.HTTP_200_OK)
                response.set_cookie(key='token', value=access_token, max_age=86400)
                return response
            else:
                return Response({'msg':'Invalid Id or password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginWorker(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            userEmail = request.data.get('email')
            userPassword = request.data.get('password')
        
            try:

                worker = Worker.objects.get(email = userEmail, password =userPassword)
            except:
                worker = None

            if worker:
                refresh = RefreshToken.for_user(user=worker)
                refresh["role"]="worker"
                access_token = str(refresh.access_token)
                response= Response({'msg':'Login Successful'}, status=status.HTTP_200_OK)
                response.set_cookie('token',access_token, secure=True, httponly=True, samesite='Strict')
                return response
            else:
                return Response({'msg':'Invalid Id or password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class profileView(APIView):
    def get(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            return Response({'msg':'Profile Page', 'data':payload}, status=status.HTTP_200_OK)
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
