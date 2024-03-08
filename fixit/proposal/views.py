from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProposalApplySerializer, ProposalApplyWorkerSerializer
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from .models import Proposal
from jobposting.models import JobRequirement
# Create your views here.


#have to edit in such a way that if the worker have already found then the user cannot apply for it.
#or just dont show it in the home page
class ProposalApplyView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                #to check if worker have already applied or not
                
                jobReqObj = JobRequirement.objects.filter(id = kwargs['id'])
                if len(jobReqObj) == 0:
                    return Response({'msg':'Job Req Not Found'}, status=status.HTTP_404_NOT_FOUND)
                if jobReqObj[0].jobStatus.lower() == "inprogress":

                    obj = Proposal.objects.filter(job_id = kwargs['id'], worker_id = payload['user_id'])
                    if len(obj)> 0:
                        return Response({'msg':'You Have Already Applied'}, status=status.HTTP_403_FORBIDDEN)
                    serilizer = ProposalApplySerializer(data=request.data)
                    if serilizer.is_valid():
                        job = kwargs['id']
                        worker = payload['user_id']
                        price = request.data.get('price')
                        description = request.data.get('description')
                        Proposal.objects.create(job_id = job, worker_id = worker, price = price, description = description)
                        return Response({'msg':'Proposal Applied successfully'})
                    return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg':'Job Requirement is no more valid'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'msg':'Only Valid to worker'}, status=status.HTTP_403_FORBIDDEN)
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
    


#shows all the proposal that have been applied for a job. But the client must be the publisher of the job requirement    
class ProposalAppliedWorkerView(APIView):
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                job = kwargs['id']    
                jobReqObj = JobRequirement.objects.filter(id = job)
                if jobReqObj[0].jobStatus.lower() == "inprogress":
                    proposalObj = Proposal.objects.filter(job_id = job, job__user_id = payload['user_id']).select_related('job')
                    serializer = ProposalApplyWorkerSerializer(proposalObj, many = True,  context = {"request":self.request})
                
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({'msg':'Worker Already Hired'}, status=status.HTTP_403_FORBIDDEN)
            return Response({'msg':'only valid to client',}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
    