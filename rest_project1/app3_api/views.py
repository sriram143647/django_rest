from django.shortcuts import render
from app3_api.models import student_data
from app3_api.serializers import student_serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.
class student_list(GenericAPIView,ListModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
class student_create(GenericAPIView,CreateModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    
class student_retrieve(GenericAPIView,RetrieveModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class student_update(GenericAPIView,UpdateModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)
    
class student_delete(GenericAPIView,DestroyModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)