from rest_framework import serializers
from .models import JobRequirement
from registration.serializer import UserModelSerializer
from category.serializer import CategoryModelSerializer

class JobRequirementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequirement
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        
        if request and request.method == "GET":
            fields['user'] = UserModelSerializer()
            fields['category'] = CategoryModelSerializer()
        
        return fields

class JobRequirementAddModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequirement
        fields = ['title','description','budget','isFeatured','latitude','longitude','location','image','category']

