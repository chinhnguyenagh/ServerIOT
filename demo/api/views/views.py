from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.serializers import *
from django.shortcuts import get_object_or_404
from smart_home.models import *

class HomeAPI(ViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]

    def list(self,request):
        homes = Home.objects.all()
        serializer = HomeSerializer(homes, many = True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        queryset = Home.objects.all()
        home = get_object_or_404(queryset, pk = pk)
        serializer = HomeSerializer(home)
        return Response(serializer.data)
    
    def update(self,request,pk):
        home = Home.objects.get(pk = pk)
        serializer = HomeSerializer(home,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DeviceAPI(ViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]

    def list(self,request):
        devices = Device.objects.all()
        serializer = DevideSerilizer(devices, many = True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        device = Device.objects.get(pk = pk)
        serializer = DevideSerilizer(device)
        return Response(serializer.data)
    
    def update(self,request,pk):
        device = Device.objects.get(pk = pk)
        serializer = DevideSerilizer(device,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    