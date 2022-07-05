from rest_framework import serializers

class student_serializer(serializers.Serializer):
    uid = serializers.IntegerField()
    name = serializers.CharField(max_length=25)
    mail = serializers.EmailField(max_length=30)
    phone = serializers.CharField(max_length=10)
    add1 = serializers.CharField(max_length=50)
    add2 = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=10)