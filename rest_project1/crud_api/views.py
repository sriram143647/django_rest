from requests import request
from django.http import HttpResponse as response
from django.http import JsonResponse as Jresponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.views import View
from crud_api.models import student_data
from crud_api.serializers import student_serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Create your views here.
# class based views
@method_decorator(csrf_exempt,name='dispatch')
class records_opr(View):
    def get(self,request,*args,**kwargs):
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id',None)
        if id is not None:
            std_data = student_data.objects.get(id=id)
            std_serializer = student_serializer(data = std_data)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
        else:
            std_data = student_data.objects.all()
            std_serializer = student_serializer(std_data,many=True)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
        
    def post(self,request,*args,**kwargs):
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        std_serializer = student_serializer(data = python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Record Inserted'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
        else:
            j_data = JSONRenderer().render(std_serializer.errors)
            return response(j_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_serializer = student_serializer(std_data,data=python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'full record updated'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
    
    def patch(self,request,*args,**kwargs):
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_serializer = student_serializer(std_data,data=python_data,partial=True)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'partial record updated'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_data.delete()
        res = {'msg':'Record updated'}
        j_data = JSONRenderer().render(res)
        return response(j_data,content_type='application/json')
    
# fuction based views
@ csrf_exempt
def record_operations(request):
    if request.method == 'GET':
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        id = python_data.get('id',None)
        if id is not None:
            std_data = student_data.objects.get(id=id)
            std_serializer = student_serializer(data = std_data)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
        else:
            std_data = student_data.objects.all()
            std_serializer = student_serializer(std_data,many=True)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
    
    if request.method == 'POST':
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        std_serializer = student_serializer(data = python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Record Inserted'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
        else:
            j_data = JSONRenderer().render(std_serializer.errors)
            return response(j_data,content_type='application/json')
    
    if request.method == 'PUT':
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_serializer = student_serializer(std_data,data=python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'full record updated'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
    
    if request.method == 'PATCH':
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_serializer = student_serializer(std_data,data=python_data,partial=True)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'partial record updated'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
    
    if request.method == 'DELETE':
        json_Data = request.body
        stream_data = io.BytesIO(json_Data)
        python_data = JSONParser().parse(stream_data)
        uid = python_data.get('uid',None)
        std_data = student_data.objects.get(uid=uid)
        std_data.delete()
        res = {'msg':'Record updated'}
        j_data = JSONRenderer().render(res)
        return response(j_data,content_type='application/json')