from django.contrib import admin
from app6_api.models import student_data

# Register your models here.
admin.site.register(student_data)
class std_api6_admin(admin.ModelAdmin):
    list_display = ['id','uid','name','mail','city']