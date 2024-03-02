from rest_framework import serializers
from .models import Proposal
from jobposting.serializer import JobRequirementModelSerializer
from registration.serializer import WorkerModelSerializer

class ProposalApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['price','description']

class ProposalApplyWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        
        if request and request.method == "GET":
            fields['job'] = JobRequirementModelSerializer()
            fields['worker'] = WorkerModelSerializer()
        
        return fields
