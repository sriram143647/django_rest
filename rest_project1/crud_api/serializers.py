from rest_framework import serializers
from crud_api.models import student_data

class student_serializer(serializers.Serializer):
    uid = serializers.IntegerField()
    name = serializers.CharField(max_length=25)
    mail = serializers.EmailField(max_length=30)
    phone = serializers.CharField(max_length=10)
    add1 = serializers.CharField(max_length=50)
    add2 = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=10)
    
    def create(self,validate_data):
        return student_data.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.uid = validated_data.get('uid',instance.uid)
        instance.name = validated_data.get('name',instance.name)
        instance.mail = validated_data.get('mail',instance.mail)
        instance.phone =validated_data.get('phone',instance.phone)
        instance.add1 = validated_data.get('add1',instance.add1)
        instance.add2 = validated_data.get('add2',instance.add2)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance