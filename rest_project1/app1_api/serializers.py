from rest_framework import serializers
from app1_api.models import student_data


#validation prority 
# 1.validators 
# 2.field level validations 
# 3.object level validation

# validators
def check_mail(value):
    if 'gmail' not in value:
        raise serializers.ValidationError("Only Gmail's are allowed")
    
def check_city(value):
    if ' ' in value:
        raise serializers.ValidationError("Space's are not allowed in city")
      
class student_serializer(serializers.Serializer):
    uid = serializers.IntegerField()
    name = serializers.CharField(max_length=25)
    mail = serializers.EmailField(max_length=30,validators=[check_mail])
    phone = serializers.CharField(max_length=10)
    add1 = serializers.CharField(max_length=50)
    add2 = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=10,validators=[check_city])
    
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
    
    # field level validation
    # def validate_uid(self,value):
    #     if value >= 50:
    #         raise serializers.ValidationError("Seat's are full")
    #     return value
    
    # field level validation
    # def validate(self, data):
    #     u = data.get('uid')
    #     ml = data.get('mail')
    #     cty = data.get('city')
    #     if 'gmail' not in ml:
    #         raise serializers.ValidationError("Only Gmail's are allowed")
    #     if ' ' in cty:
    #         raise serializers.ValidationError("Space's are not allowed in city")
    #     if u >= 50:
    #         raise serializers.ValidationError("Seat's are full")
    #     else:
    #         return data
    
