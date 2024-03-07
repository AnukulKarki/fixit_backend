from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializer import UserModelSerializer, UserLoginSerializer
from .models import  User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import verify_access_token 
# Create your views here.

class RegistrationUser(CreateAPIView):
    def post(self, request):
        serializer = UserModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                role = ""
                refresh = RefreshToken.for_user(user=user)
                if user.role.lower() == "client":
                    refresh["role"]="client"
                    role = "client"
                else:
                    refresh['role'] = "worker"
                    role = "worker"
                access_token = str(refresh.access_token)
                response= Response({'msg':'Login Successful','token':access_token, 'role':role}, status=status.HTTP_200_OK)
                response.set_cookie(key='token', value=access_token, secure=True, httponly=True, samesite="None")
                return response
            else:
                return Response({'msg':'Invalid Id or password'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class profileView(APIView):
    def get(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == 'user':
                user = User.objects.get(User_id=payload['user_id'])
                serializer = UserModelSerializer(user, context = {"request":self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            # else:
            #     worker = Worker.objects.get(worker_id=payload['user_id'])
            #     serializer = WorkerModelSerializer(worker, context = {"request":self.request})
                # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request):
        response = Response({"msg":"Log out successfully"}, status=status.HTTP_200_OK)
        response.delete_cookie('token')
        return response
    
class UserCheck(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                return Response({"role":"client"}, status=status.HTTP_200_OK)
            elif payload['role'].lower() == "worker":
                return Response({"role":"worker"}, status=status.HTTP_200_OK)
            return Response({"msg":"Un-authorized user"}, status=status.HTTP_401_UNAUTHORIZED) 
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
          