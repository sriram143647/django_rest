from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api1.models import employee

# Register your models here.
class emp_admin(UserAdmin):
    model = employee
    list_display = ["name", "mail", "phone", "gender"]

admin.site.register(employee, emp_admin)
