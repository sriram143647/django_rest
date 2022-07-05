from django.shortcuts import render
from requests import request
from django.http import HttpResponse as response
from django.http import JsonResponse as Jresponse
from app1_api import serializers
from app1_api.models import student_data
from app1_api.serializers import student_serializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def student_details(request):
    std_data = student_data.objects.all()
    std_serializer = student_serializer(std_data,many=True)
    # j_data = JSONRenderer().render(std_serializer.data)
    # return response(j_data,content_type='application/json')
    return Jresponse(std_serializer.data)

def student_detail(request,pk):
    std_data = student_data.objects.get(uid=pk)
    std_serializer = student_serializer(std_data)
    # j_data = JSONRenderer().render(std_serializer.data)
    # return response(j_data,content_type='application/json')
    return Jresponse(std_serializer.data,safe=False)