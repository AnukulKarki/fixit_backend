from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProposalApplySerializer, ProposalApplyWorkerSerializer
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from .models import Proposal
# Create your views here.

class ProposalApplyView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "worker":
                serilizer = ProposalApplySerializer(data=request.data)
                if serilizer.is_valid():
                    job = kwargs['id']
                    worker = payload['user_id']
                    price = request.data.get('price')
                    description = request.data.get('description')
                    Proposal.objects.create(job_id = job, worker_id = worker, price = price, description = description)
                    return Response({'msg':'Proposal Applied successfully'})
                return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'msg':'Only Valid to User'}, status=status.HTTP_403_FORBIDDEN)
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
    
class ProposalAppliedWorkerView(APIView):
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            job = kwargs['id']    
            proposalObj = Proposal.objects.filter(job_id = job)
            serializer = ProposalApplyWorkerSerializer(proposalObj, many = True,  context = {"request":self.request})
                
            return Response({'proposal':serializer.data,}, status=status.HTTP_200_OK)
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)
    