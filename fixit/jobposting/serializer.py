from rest_framework import serializers
from .models import JobRequirement, JobApply, Job

class JobRequirementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequirement
        fields = "__all__"

class JobRequirementAddModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRequirement
        fields = ['title','description','budget','isFeatured','latitude','longitude','location','image','category']


class JobApplyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApply
        fields = "__all__"

class Job(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
