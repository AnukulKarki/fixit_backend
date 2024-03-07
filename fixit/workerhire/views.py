from django.shortcuts import render
from rest_framework.views import APIView
from proposal.serializer import ProposalApplySerializer, ProposalApplyWorkerSerializer
from registration.utils import verify_access_token
from rest_framework.response import Response
from rest_framework import status
from proposal.models import Proposal
from django.utils import timezone

# Create your views here.

class WorkerHire(APIView):
     def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("token", None)
        verification, payload = verify_access_token(token) 
        if verification:
            if payload['role'].lower() == "client":
                proposalId = kwargs['id']
                jobId = kwargs['jobid']
               

                
                proposalObj = Proposal.objects.filter(id = proposalId)
                if len(proposalObj) == 0:
                    return Response({'msg':'not found'}, status=status.HTTP_404_NOT_FOUND)
                if proposalObj[0].job.user_id == payload['user_id']:
                    proposalObj.update(status = "accept", accepted_at = timezone.now)
                    proposalObjToUpdate = Proposal.objects.exclude(id = proposalId).filter(job_id = jobId)
                    proposalObjToUpdate.update(status = "rejected")
                    return Response({'msg':'Worker Hired Successfully'}, status = status.HTTP_200_OK)


               
                return Response({'msg':'Un Authorized user'},status=status.HTTP_404_NOT_FOUND)
            return Response({'msg':'Only Valid to client'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"msg":"Login first"}, status=status.HTTP_401_UNAUTHORIZED)