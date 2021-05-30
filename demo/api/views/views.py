from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.serializers import *
from django.shortcuts import get_object_or_404

class UpdateHomeStatus(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]

    def get(self,request, pk):
        home = get_object_or_404(Home, pk =pk)
        serializer = HomeSerializer(home)
        
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self,request,pk):
        home = get_object_or_404(Home,pk = pk)
        serializer = HomeSerializer(home, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UpdateStatusDevide(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]

    def get(self,request,devide_id):
        devide = get_object_or_404(Devide,pk = devide_id)
        serializer = DevideSerilizer(devide)
        return Response(serializer.data, status =status.HTTP_200_OK)

    def put(self,request,devide_id):
        devide = get_object_or_404(Devide, pk = devide_id)
        seri = DevideSerilizer(devide, data = request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status = status.HTTP_200_OK)
        else:
            return Response(seri.errors, status = status.HTTP_400_BAD_REQUEST)