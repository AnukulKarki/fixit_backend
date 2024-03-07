from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView
from .serializer import gigModelSerializer, gigModelAddSerializer
from .models import gig 




class GigPostView(APIView):
    def post(self,request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                workerId = payload['user_id']
                serializer = gigModelAddSerializer(data = request.data)
                if serializer.is_valid():
                    userTitle = serializer.data.get("title")
                    userDescription = serializer.data.get("description")    
                    userCategory = serializer.data.get("category")
                    userImage = serializer.data.get("image")
                    gig.objects.create(title = userTitle, description = userDescription, category_id = userCategory, image = userImage, worker_id = workerId )
                    return Response({'msg':'Successfully Updated'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'msg':'Only Valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)           

        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigListView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            gigData = gig.objects.filter(worker_id = payload['user_id'])
            serializer = gigModelSerializer(gigData, many = True, context = {"request":self.request})

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"Login First"}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigListAllView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            gigData = gig.objects.all()
            serializer = gigModelSerializer(gigData, many = True, context = {"request":self.request})

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"Login First"}, status=status.HTTP_401_UNAUTHORIZED)
#code to edit the gig
class GigEditView(UpdateAPIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                # try:
                gigObject = gig.objects.filter(id=kwargs['id'])
                if len(gigObject) ==0:
                    return Response({'msg':'gig not found'}, status=status.HTTP_404_NOT_FOUND)
                if gigObject[0].worker == payload['user_id']:

                    serializer = gigModelAddSerializer(data = request.data)
                    if serializer.is_valid():
                        updatedTitle = request.data.get("title")
                        updatedDescription = request.data.get("description")
                        updatedCategory = request.data.get("category")
                        updatedImage = request.data.get("image")
                        gigObject.update(title=updatedTitle, description = updatedDescription, category_id = updatedCategory, image = updatedImage, worker_id = payload['user_id'])
                        return Response({"detail":"updated Successfull"}, status=status.HTTP_200_OK)
                return Response({'msg':'Only Valid to owner'}, status=status.HTTP_401_UNAUTHORIZED)    

                # except:
                    # return Response({"detail":"Gig not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({"detail":"Only valid to worker"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"detail":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
        
#code to delete the gig
class GigDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                try:
                    gigObj = gig.objects.get(id=kwargs['id'])
                    if gigObj.worker ==  payload['user_id']:
                        gigObj.delete()
                        return Response({"detail":"Delete Successfully"}, status=status.HTTP_200_OK)
                    else:
                        return Response({"detail":"Only valid to owner"}, status=status.HTTP_401_UNAUTHORIZED)
                except:
                    return Response({"detail":"Gig not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"detail":"Only valid to worker"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"detail":"Login with worker first"}, status=status.HTTP_401_UNAUTHORIZED)
    

class GigDetailView(APIView):
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                try:
                    gigObject = gig.objects.get(id=kwargs['id'])
                    
                    serializer = gigModelSerializer(gigObject, context = {"request":self.request})
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return Response({"detail":"Gig Not Found "}, status=status.HTTP_404_NOT_FOUND)        
            return Response({"detail":"Only valid to worker "}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"detail":"Worker is not login"}, status=status.HTTP_401_UNAUTHORIZED)
        