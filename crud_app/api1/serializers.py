from rest_framework import serializers
from api1.models import employee
    
class emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id','name','mail','phone','gender','add']