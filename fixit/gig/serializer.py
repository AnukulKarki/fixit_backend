from .models import gig
from rest_framework import serializers
from registration.serializer import WorkerModelSerializer,CategoryModelSerializer

class gigModelSerializer(serializers.ModelSerializer):
    # worker = WorkerModelSerializer(many = True)
    # category = CategoryModelSerializer(many = True)
    class Meta:
        model = gig
        fields = '__all__'