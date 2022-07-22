from api1.models import employee
from api1.serializers import emp_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# # function based APIview
@api_view(['GET','POST','PUT','DELETE'])
def rec_operations(request,id=None):
    if request.method == 'GET':
        if id is not None:
            std_data = employee.objects.get(id=id)
            std_serializer = emp_serializer(std_data)
            return Response(std_serializer.data)
        else:
            std_data = employee.objects.all()
            std_serializer = emp_serializer(std_data,many=True)
            return Response(std_serializer.data)
    
    if request.method == 'POST':
        std_serializer = emp_serializer(data = request.data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'New Record Inserted'}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response(std_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT':
        std_data = employee.objects.get(id=id)
        std_serializer = emp_serializer(std_data,data=request.data)
        if std_serializer.is_valid():
            std_serializer.save()
            res = {'msg':'Full Record Updated'}
            return Response(res,status=status.HTTP_201_CREATED)
        else:
            return Response(std_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        std_data = employee.objects.get(id=id)
        std_data.delete()
        res = {'msg':'Record Deleted'}
        return Response(res,status=status.HTTP_201_CREATED)