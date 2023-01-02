from app2_api.models import student_data
from app2_api.serializers import student_serializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# function based APIview
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def rec_operations(request,id=None):
    if request.method == 'GET':
        if id is not None:
            std_data = student_data.objects.get(uid=id)
            std_serializer = student_serializer(std_data)
            return Response(std_serializer.data)
        else:
            std_data = student_data.objects.all()
            std_serializer = student_serializer(std_data,many=True)
            return Response(std_serializer.data)
    
    if request.method == 'POST':
        std_serializer = student_serializer(data = request.data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'New Record Inserted'}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response(std_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        std_data = student_data.objects.get(uid=id)
        std_serializer = student_serializer(std_data,data=request.data,partial=True)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Partial Record Updated'}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response(std_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT':
        std_data = student_data.objects.get(uid=id)
        std_serializer = student_serializer(std_data,data=request.data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Full Record Updated'}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response(std_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        std_data = student_data.objects.get(uid=id)
        std_data.delete()
        res = {'msg':'Record Deleted'}
        return Response(res,status=status.HTTP_201_CREATED)