from django.shortcuts import render
from rest_framework.response import Response
from app6_api.models import student_data
from app6_api.serializers import student_serializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from app6_api.permissions import my_permission

# Create your views here.
class student_model_viewset(viewsets.ModelViewSet):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [my_permission]