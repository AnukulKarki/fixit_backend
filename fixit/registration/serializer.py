from rest_framework import serializers
from .models import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class WorkerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"