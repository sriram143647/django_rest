from django.contrib import admin
from app7_api.models import student_detail,class_detail

# Register your models here.
admin.site.register(student_detail)
class std_admin_table(admin.ModelAdmin):
    list_display = ['id','roll_no','name','mail','std_class']

admin.site.register(class_detail)
class class_admin_table(admin.ModelAdmin):
    list_display = ['id','room_no','teacher_name','class_room']