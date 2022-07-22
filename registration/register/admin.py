from django.contrib import admin
from register.models import employee

# Register your models here.
@admin.register(employee)
class std_admin(admin.ModelAdmin):
    list_display = ['id','name','email','phone']