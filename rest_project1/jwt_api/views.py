from django.shortcuts import render
from jwt_api.models import student_data
from jwt_api.serializers import student_serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class student_list_create(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
        
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    
class student_retrieve_update_delete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)