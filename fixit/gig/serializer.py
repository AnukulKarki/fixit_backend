from .models import gig
from rest_framework import serializers
from registration.serializer import UserModelDataSerializer
from category.serializer import CategoryModelSerializer


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
            fields['worker'] = UserModelDataSerializer()
            fields['category'] = CategoryModelSerializer()
        
        return fields

class gigModelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = gig
        fields = ['title','description','category','image']