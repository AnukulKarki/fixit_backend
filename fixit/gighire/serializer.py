from rest_framework import serializers
from .models import GigProposal, Rating
from registration.serializer import UserModelDataSerializer
from category.serializer import CategoryModelSerializer

class GigProposalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigProposal
        fields = '__all__'
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        
        if request and request.method == "GET":
            fields['worker'] = UserModelDataSerializer()
            fields['user'] = UserModelDataSerializer()
            fields['category'] = CategoryModelSerializer()
        
        return fields


class GigProposalModelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigProposal
        fields = ['worktitle','workdescription','location','latitude','longitude','image']



class GigProposalModelPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GigProposal
        fields = ['payamount','paymethod']

    
class RateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rate']