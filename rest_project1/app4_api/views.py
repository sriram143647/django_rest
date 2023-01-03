from app4_api.models import student_data
from app4_api.serializers import student_serializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# generate token in termianl
# python manae.py drf_create_token username

# Create your views here.
class student_list_create(ListCreateAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
class student_retrieve_update_delete(RetrieveUpdateDestroyAPIView):
    queryset = student_data.objects.all()
    serializer_class = student_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]