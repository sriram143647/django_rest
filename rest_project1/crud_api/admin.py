from django.contrib import admin
from crud_api.models import student_data

# Register your models here.
@admin.register(student_data)
class std_admin(admin.ModelAdmin):
    list_display = ['id','uid','name','mail','city']