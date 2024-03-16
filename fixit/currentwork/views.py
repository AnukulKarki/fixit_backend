from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from proposal.models import Proposal
from proposal.serializer import ProposalApplyWorkerSerializer
from jobposting.models import JobRequirement
from .serializer import PayModelSerializer
from gighire.models import Rating
from gighire.serializer import RateModelSerializer
from registration.models import User 
class CurrentWorkerWorkView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                workData = Proposal.objects.filter(worker_id = payload['user_id'])
                workerCurrentData = workData.exclude(status="rejected").exclude(status="payed").exclude('cancel')
                serializer = ProposalApplyWorkerSerializer(workerCurrentData, many= True, context = {"request":self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'msg':'only valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

class CurrentWorkerClientView(APIView):
    def get(self, request):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                jobId = Proposal.objects.filter(job__user_id = payload['user_id']).select_related('job')
                jobIdActive = jobId.exclude(status="rejected").exclude(status="payed").exclude('cancel')
                serializer = ProposalApplyWorkerSerializer(jobIdActive, many= True, context = {"request":self.request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'msg':'only valid to Client'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

class CancelCurrentWorkerView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                
                workId  = Proposal.objects.filter(id = kwargs['id'], worker_id = payload['user_id'])
                if len(workId) == 0:
                    return Response({'msg':'Work Not found'})
                if workId[0].status.lower() != "accept":
                    return Response({'msg':'Cannot Cancel the work'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                workId.update(status="cancel")
                JobRequirement.objects.filter(id = workId[0].job_id).update(jobStatus="cancel")
                return Response({'msg':'Job Cancelled Successfully'}, status=status.HTTP_200_OK)    
            return Response({'msg':'only valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

#Start the work
class startCurrentWorkerView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                workId  = Proposal.objects.filter(id = kwargs['id'], worker_id = payload['user_id'])
                if len(workId) == 0:
                    return Response({'msg':'Work Not found'})
                if workId[0].status.lower() == "accept":
                    workId.update(status="started")
                    return Response({'msg':'Job Started Successfully'}, status=status.HTTP_200_OK) 
                return Response({'msg':'Cannot Start the work'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                   
            return Response({'msg':'only valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)

#complete the current work
class CompleteCurrentWorkerView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                workId  = Proposal.objects.filter(id = kwargs['id'], worker_id = payload['user_id'])
                if len(workId) == 0:
                    return Response({'msg':'Work Not found'})
                if workId[0].status.lower() == "started":
                    workId.update(status="completed")
                    return Response({'msg':'Job completed Successfully'}, status=status.HTTP_200_OK) 
                return Response({'msg':'Cannot Start the work'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                   
            return Response({'msg':'only valid to worker'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)
    

class PayWorkView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                workId  = Proposal.objects.filter(id = kwargs['id'])
                if len(workId) == 0:
                    return Response({'msg':'Work Not found'})
                if workId[0].status.lower() == "completed":
                    #pay The worker using cash
                    serailizer = PayModelSerializer(data = request.data)
                    if serailizer.is_valid():
                        amount = request.data.get('amountPayed')
                        method = request.data.get('paymethod')
                        workId.update(amountPayed = amount, paymethod = method, status = 'payed')
                        JobRequirement.objects.filter(id = workId[0].job_id).update(jobStatus="completed")

                        return Response({'msg':'Amount Payed Successfully'}, status=status.HTTP_200_OK) 
                    return Response(serailizer.errors, status=status.HTTP_200_OK) 
                return Response({'msg':'Work Is not complete yet'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response({'msg':'only valid to User'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)


class RatingView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            workId = None
            if payload['role'].lower() == "worker":
                workId  = Proposal.objects.filter(id = kwargs['id'], worker_id = payload['user_id'])
            else:
                workId  = Proposal.objects.filter(id = kwargs['id'], job__user_id = payload['user_id']).select_related('job')

            if len(workId) == 0:
                return Response({'msg':'Work Not found'}, status=status.HTTP_404_NOT_FOUND)
            if workId[0].status.lower() == "payed":

                rateObj = Rating.objects.filter(rateuser_id = payload['user_id'], jobproposal_id = workId[0].job_id )
                if len(rateObj) > 0:
                    return Response({'msg':'Already Rated The user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer = RateModelSerializer(data = request.data)
                if serializer.is_valid():
                    rate = request.data.get('rate')
                    rateduser = None
                    if payload['role'].lower() == "worker":
                        rateduser = workId[0].job.user_id
                        Rating.objects.create(rateuser_id = payload['user_id'], jobproposal_id = workId[0].job_id ,rateduser_id = rateduser, rate = rate)
                    else:
                        rateduser = workId[0].worker_id
                        Rating.objects.create(rateuser_id = payload['user_id'], jobproposal_id = workId[0].job_id ,rateduser_id = rateduser, rate = rate)

                    rateData  = Rating.objects.filter(rateduser_id = rateduser)
                    totalRating = 0
                    for rateObj in rateData:
                        totalRating += rateObj.rate
                    avg = totalRating/len(rateData)
                    User.objects.filter(id =rateduser ).update(rating = avg)
                        

                    return Response({'msg':'Rated Successfully'}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



            return Response({'msg':'Cannot Rate'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
        return Response({'msg':'Login First'}, status=status.HTTP_401_UNAUTHORIZED)




class PastWorkView(APIView):
    def get(self, request):
        pass
