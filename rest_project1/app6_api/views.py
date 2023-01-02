from django.shortcuts import render
from rest_framework.response import Response
from app6_api.models import student_data
from app6_api.serializers import student_serializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class student_read_only_model_viewset(viewsets.ViewSet):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]