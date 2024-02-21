from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from .serializer import JobApplyModelSerializer


#Job requirement Posting
class JobRequirementPostView(APIView):
    def post(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "user":
                serializer = JobApplyModelSerializer
                if serializer.is_valid:
                    pass



        # return Response({'msg':'Profile Page', 'userid':workerId, 'role':'worker'}, status=status.HTTP_200_OK)
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

#All Job Requirement Post
class JobRequirementListView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
#Job Requirement Details of particular loged in user only
class JobRequirementListViewUser(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
    

#Job Requirement Edit 
class JobRequirementEditView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
#Job Requirmeent Delete
class JobRequirementDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
#Job Requirement delete
class JobRequirementDelete(APIView):
    def post(self, request, *args, **kwargs):
        
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
#Job Requirement Detail
class JobRequirementDetailView(APIView):
    def get(self, request, *args, **kwargs):
        
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            pass
        
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    

