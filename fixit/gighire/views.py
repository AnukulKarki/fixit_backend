from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .serializer import GigProposalModelAddSerializer, GigProposalModelSerializer, GigProposalModelPaySerializer, RateModelSerializer
from .models import GigProposal
from datetime import datetime
from .models import Rating
from registration.models import User

class GigProposalApplyView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                serializer = GigProposalModelAddSerializer(data = request.data)
                if serializer.is_valid():
                    title = request.data.get('worktitle')
                    description = request.data.get('workdescription')
                    location = request.data.get('location')
                    latitude = request.data.get('latitude')
                    longitude = request.data.get('longitude')
                    image = request.data.get('image')
                    category = request.data.get('category')
                    GigProposal.objects.create(worker_id = kwargs['id'], user_id = payload['user_id'],category_id = category ,worktitle = title, workdescription = description, location =location, latitude = latitude, longitude = longitude, image = image)
                    return Response({'msg':'Proposal Submit Successfully'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg':'Only valid to client'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

class GigProposalListview(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                gigProposalView = GigProposal.objects.filter(worker_id = payload['user_id'], status = "applied")
                
                if len(gigProposalView) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                serializer = GigProposalModelSerializer(gigProposalView, many = True, context = {'request':self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigProposalAcceptView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "applied":
                    GigProposalObj.update(status="accept", acceptedate = datetime.now)
                return Response({'msg':'cant accept the proposal'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigProposalRejectView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "applied":
                    GigProposalObj.update(status="reject")
                return Response({'msg':'Proposal Rejected'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class CurrentGigWorkView(APIView):
    def post(self, request,):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(worker_id = payload['user_id'])
                CurrentGigWork = GigProposalObj.exclude(status='cancel').exclude(status='payed').exclude(status='rejected')
                
                if len(CurrentGigWork) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                serializer = GigProposalModelSerializer(CurrentGigWork, many = True, context = {'request':self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class CurrentGigWorkClientView(APIView):
    def post(self, request,):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client": 
                GigProposalObj = GigProposal.objects.filter(user_id = payload['user_id'])
                CurrentGigWork = GigProposalObj.exclude(status='cancel').exclude(status='payed').exclude(status='rejected')
                
                if len(CurrentGigWork) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                serializer = GigProposalModelSerializer(CurrentGigWork, many = True, context = {'request':self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    

class GigWorkStartView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "accept":
                    GigProposalObj.update(status="started")
                return Response({'msg':'Work Started'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)


class GigWorkCompleteView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "started":
                    GigProposalObj.update(status="completed")
                return Response({'msg':'Work Completed'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    
class GigWorkCancelView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "accept":
                    GigProposalObj.update(status="cancel")
                return Response({'msg':'Work cancel'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    

class GigWorkPayView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client": 
                GigProposalObj = GigProposal.objects.filter(id = kwargs['id'])
                if len(GigProposalObj) == 0:
                    return Response({'msg':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if GigProposalObj[0].status.lower() == "completed":
                    serializer = GigProposalModelPaySerializer(data = request.data)
                    if serializer.is_valid():
                        amount = request.data.get('payamount')
                        method = request.data.get('paymethod')
                        GigProposalObj.update(status="payed", payamount = amount, paymethod = method)

                        return Response({'msg':'Payment Successfull'}, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg':'Cannot Pay'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'msg':'Only valid to Worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    

class RatingView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            gigJobObj = None
            if payload['role'].lower() == "worker":
                gigJobObj = GigProposal.objects.filter(id = kwargs['id'], worker_id = payload['user_id'])
            else:
                gigJobObj = GigProposal.objects.filter(id = kwargs['id'], user_id = payload['user_id'])
            
            if gigJobObj[0].status.lower() == "payed":
                rateObj = Rating.objects.filter(rateuser_id = payload['user_id'], gigproposal_id = kwargs['id'])
                if len(rateObj) >0:
                    return Response({'msg':'You have already rated the user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer = RateModelSerializer(data = request.data)
                if serializer.is_valid():
                    rate = request.data.get('rate')
                    if payload['role'].lower() == "worker":
                        rateduser = gigJobObj[0].user_id
                        Rating.objects.create(rateuser_id = payload['user_id'], gigproposal_id = kwargs['id'],rateduser_id = rateduser, rate = rate)
                    else:
                        rateduser= gigJobObj[0].worker_id
                        Rating.objects.create(rateuser_id = payload['user_id'], gigproposal_id = kwargs['id'],rateduser_id = rateduser, rate = rate)

                    rateData  = Rating.objects.filter(rateduser_id = rateduser)
                    totalRating = 0
                    for rateObj in rateData:
                        totalRating += rateObj.rate
                    avg = totalRating/len(rateData)
                    User.objects.filter(id =rateduser ).update(rating = avg)

                    return Response({'msg':'Rated Successfully'}, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'msg':'Cannot Rate'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)