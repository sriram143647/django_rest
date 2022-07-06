"""rest_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1_api import views as app1_views
from crud_api import views as crud_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std_infos/',app1_views.student_details),
    path('std_info/<int:pk>',app1_views.student_detail),
    path('rec_create/',app1_views.record_create),
    path('get_data/',app1_views.record_fetch),
    path('crud_api/',crud_views.record_operations),
    # path('crud_api/',crud_views.records_opr.as_view()),
]
