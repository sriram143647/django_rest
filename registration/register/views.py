from register.models import employee
from register.serializers import emp_serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse as response
import io

# fuction based views
@ csrf_exempt
def rec_operations(request):
    json_Data = request.body
    stream_data = io.BytesIO(json_Data)
    python_data = JSONParser().parse(stream_data)

    if request.method == 'GET':
        email = python_data.get('email',None)
        if email == '':
            email = None 
        if email is not None:
            std_data = employee.objects.get(email=email)
            std_serializer = emp_serializer(std_data)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
        else:
            std_data = employee.objects.all()
            std_serializer = emp_serializer(std_data,many=True)
            j_data = JSONRenderer().render(std_serializer.data)
            return response(j_data,content_type='application/json')
    
    if request.method == 'POST':
        std_serializer = emp_serializer(data = python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Record Inserted'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
        else:
            j_data = JSONRenderer().render(std_serializer.errors)
            return response(j_data,content_type='application/json')
    
    if request.method == 'PUT':
        email = python_data.get('email',None)
        std_data = employee.objects.get(email=email)
        std_serializer = emp_serializer(std_data,data=python_data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'full record updated'}
            j_data = JSONRenderer().render(res)
            return response(j_data,content_type='application/json')
    
    if request.method == 'DELETE':
        email = python_data.get('email',None)
        std_data = employee.objects.get(email=email)
        std_data.delete()
        res = {'msg':'Record updated'}
        j_data = JSONRenderer().render(res)
        return response(j_data,content_type='application/json')