from unicodedata import name
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from register.models import employee
    
class emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
        
        # extra_kwargs = {
        #     'name':{'required':True},
        #     'email':{'required':True},
        #     'phone':{'required':True},
        # }