from rest_framework import serializers
from app3_api.models import student_data

# validators    
class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = student_data
        fields = ['uid','name','mail','phone','city']
        
    extra_kwargs = {'uid':{'read-only':True}}