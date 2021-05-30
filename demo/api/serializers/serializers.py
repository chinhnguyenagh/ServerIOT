from rest_framework.serializers import ModelSerializer
from smart_home.models import *

class DevideSerilizer(ModelSerializer):
    class Meta:
        model = Devide
        fields = ['status','auto']

class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = ['temperature', 'humid', 'distance_door','distance_private_room']