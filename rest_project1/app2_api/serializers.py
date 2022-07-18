from rest_framework import serializers
from app2_api.models import student_data

# validators
def check_mail(value):
    if 'gmail' not in value:
        raise serializers.ValidationError("Only Gmail's are allowed")
    
def check_city(value):
    if ' ' in value:
        raise serializers.ValidationError("Space's are not allowed in city")
    
class student_serializer(serializers.ModelSerializer):
    mail = serializers.EmailField(max_length=30,validators=[check_mail])
    city = serializers.CharField(max_length=10,validators=[check_city])
    class Meta:
        model = student_data
        fields = ['uid','name','mail','phone','city']
        
    extra_kwargs = {'uid':{'read-only':True}}