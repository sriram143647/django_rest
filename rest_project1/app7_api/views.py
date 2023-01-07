from django.shortcuts import render
from rest_framework.response import Response
from app7_api.models import student_detail,class_detail
from app7_api.serializer import student_serializer,class_serializer
from rest_framework import viewsets

# Create your views here.
class student_model_viewset(viewsets.ModelViewSet):
    queryset = student_detail.objects.all()
    serializer_class = student_serializer
    
class class_room_model_viewset(viewsets.ModelViewSet):
    queryset = class_detail.objects.all()
    serializer_class = class_serializer
