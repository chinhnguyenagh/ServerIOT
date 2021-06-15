from rest_framework.serializers import ModelSerializer
from smart_home.models import *

class DevideSerilizer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'