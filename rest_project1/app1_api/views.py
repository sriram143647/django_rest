from django.http import HttpResponse as response
from django.http import JsonResponse as Jresponse
from django.views.decorators.csrf import csrf_exempt
from app1_api.models import student_data
from app1_api.serializers import student_serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from requests import request

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

def record_fetch(request):
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

@ csrf_exempt
def record_create(request):
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