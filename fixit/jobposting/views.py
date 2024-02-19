from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status



class jobPostView(APIView):
    def get(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                workerId = payload['user_id']
            return Response({'msg':'Profile Page', 'userid':workerId, 'role':'worker'}, status=status.HTTP_200_OK)
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
