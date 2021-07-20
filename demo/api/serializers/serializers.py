from rest_framework.serializers import ModelSerializer, Serializer
from smart_home.models import *
from rest_framework import serializers

class DevideSerilizer(ModelSerializer):
     
    class Meta:
        model = Device
        exclude = ['esp']
class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class EspSerializer(serializers.ModelSerializer):
    list_device = DevideSerilizer(many = True)

    class Meta:
        model = Esp
        fields = '__all__'