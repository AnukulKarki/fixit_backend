from rest_framework import serializers
from proposal.models import Proposal
class PayModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['amountPayed', 'paymethod']