from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from registration.models import Worker, WorkerProfile
from rest_framework.generics import ListAPIView
from .serializer import gigModelSerializer
from .models import gig 



class GigPostView(APIView):
    def post(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                serializer = gigModelSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Successfully Updated'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response({'msg':'Only Valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)           

        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigListView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            gigData = gig.objects.all()
            serializer = gigModelSerializer(gigData, many = True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"Login First"}, status=status.HTTP_401_UNAUTHORIZED)
