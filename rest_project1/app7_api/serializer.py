from rest_framework import serializers
from app7_api.models import student_detail,class_detail

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = student_detail
        fields = ['roll_no','name','mail']
            
class class_serializer(serializers.ModelSerializer):
    std_data = serializers.StringRelatedField(many=True,read_only=True)
    # std_data = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # std_data = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='std_data-detail')
    # std_data = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    # std_data = serializers.HyperlinkedIdentityField(view_name='std_detail-list')
    # std_data = serializers.HyperlinkedIdentityField(view_name='std_detail-list')
    class Meta:
        model = class_detail
        fields = ['room_no','teacher_name','class_room','std_data']
        
# anoter way to get yperlinked fields
# class class_serializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = class_detail
#         fields = ['room_no','teacher_name','class_room','std_data']