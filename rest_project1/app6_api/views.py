from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.response import Response
from app1_api import serializers
from app6_api.models import student_data
from app6_api.serializers import student_serializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class student_read_only_model_viewset(viewsets.ReadOnlyModelViewSet):
    queryset = student_data.objects.all()
    serializer_class = student_serializer