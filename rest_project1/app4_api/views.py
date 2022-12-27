from app4_api.models import student_data
from app4_api.serializers import student_serializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class student_list(ListAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_create(CreateAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_retrieve(RetrieveAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_update(UpdateAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_delete(DestroyAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_list_create(ListCreateAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_retrieve_destroy(RetrieveDestroyAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_retrieve_update(RetrieveUpdateAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    
class student_retrieve_update_delete(RetrieveUpdateDestroyAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer