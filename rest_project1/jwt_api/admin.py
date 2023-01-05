from django.contrib import admin
from jwt_api.models import student_data

# Register your models here.
admin.site.register(student_data)
class jwt_api_admin(admin.ModelAdmin):
    list_display = ['id','uid','name','mail','city']