from django.shortcuts import render
from rest_framework.response import Response
from app5_api.models import student_data
from app5_api.serializers import student_serializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class student_viewset(viewsets.ViewSet):
    def list(self,request):
        std_data = student_data.objects.all()
        serializer_data = student_serializer(std_data,many=True)
        return Response(serializer_data.data)
    
    def create(self,request):
        serializers_data = student_serializer(data=request.data)
        if serializers_data.is_valid:
            serializers_data.save()
            return Response({'msg':'Record Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request,pk=None):
        id = pk
        if id is not None:
            std_data = student_data.objects.get(id=id)
            serializer_data = student_serializer(std_data)
            return Response(serializer_data.data)
        
    def update(self, request,pk=None):
        id = pk
        if id is not None:
            std_data = student_data.objects.get(id=id)
            serializer_data = student_serializer(std_data,data=std_data)
            if serializer_data.is_valid:
                serializer_data.save()
                return Response({'msg':'Full Record Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def partial_update(self, request,pk=None):
        id = pk
        if id is not None:
            std_data = student_data.objects.get(id=id)
            serializer_data = student_serializer(std_data,data=std_data,partial=True)
            if serializer_data.is_valid:
                serializer_data.save()
                return Response({'msg':'Partial Record Updated'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request,pk=None):
        id = pk
        if id is not None:
            std_data = student_data.objects.get(id=id)
            std_data.delete()
            return Response({'msg':'Record Deleted'},status=status.HTTP_201_CREATED)