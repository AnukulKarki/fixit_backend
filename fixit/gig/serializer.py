from .models import gig
from rest_framework import serializers
from registration.serializer import WorkerModelSerializer,CategoryModelSerializer
from registration.models import Worker

class WorkerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["id","email","firstname", "lastname", "phone"]

class gigModelSerializer(serializers.ModelSerializer):
    # worker = WorkerModelSerializer(many = True)
    # category = CategoryModelSerializer(many = True)
    class Meta:
        model = gig
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        
        if request and request.method == "GET":
            fields['worker'] = WorkerModelSerializer()
            fields['category'] = CategoryModelSerializer()
        
        return fields

class gigModelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = gig
        fields = ['title','description','category','image']