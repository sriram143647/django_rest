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
from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from crud_api import views as crud_views
from app1_api import views as app1_views
from app2_api import views as app2_views
from app3_api import views as app3_views
from app4_api import views as app4_views
from app5_api import views as app5_views
from app6_api import views as app6_views
from app4_api.auth_token import modified_token

#router object
my_router = DefaultRouter()

#register viewset wit router
my_router.register('api5',app5_views.student_viewset,basename='std')
# my_router.register('api6',app6_views.student_model_viewset,basename='std')

urlpatterns = [
    path('admin/', admin.site.urls),
    #api1 urls
    path('std_infos/',app1_views.student_details),
    path('std_info/<int:pk>',app1_views.student_detail),
    path('rec_create/',app1_views.record_create),
    path('get_data/',app1_views.record_fetch),
    
    #crud api urls
    path('crud_api/',crud_views.record_operations),
    # path('crud_api/',crud_views.records_opr.as_view()),
    
    #api2 urls
    path('api2/',app2_views.rec_operations),
    path('api2/<int:id>/',app2_views.rec_operations),
    
    # api3 urls
    # path('api3/',app3_views.student_list.as_view()),
    # path('api3/',app3_views.student_create.as_view()),
    # path('api3/<int:pk>/',app3_views.student_retrieve.as_view()),
    # path('api3/<int:pk>/',app3_views.student_update.as_view()),
    # path('api3/<int:pk>/',app3_views.student_delete.as_view()),
    path('api3/',app3_views.student_list_create.as_view()),
    path('api3/<int:pk>/',app3_views.student_retrieve_update_delete.as_view()),
    
    #api4 urls
    # path('api4/',app4_views.student_list.as_view()),
    # path('api4/',app4_views.student_create.as_view()),
    path('api4/',app4_views.student_list_create.as_view()),
    # path('api4/<int:pk>/',app4_views.student_retrieve.as_view()),
    # path('api4/<int:pk>/',app4_views.student_update.as_view()),
    # path('api4/<int:pk>/',app4_views.student_delete.as_view()),
    # path('api4/<int:pk>/',app4_views.student_retrieve_destroy.as_view()),
    # path('api4/<int:pk>/',app4_views.student_retrieve_update.as_view()),
    path('api4/<int:pk>/',app4_views.student_retrieve_update_delete.as_view()),
    path('get-token/',obtain_auth_token),
    # path('get-token/',modified_token.as_view()),
        
    #api5 urls
    path('',include(my_router.urls)),
    
    #api6 urls
    # path('',include(my_router.urls)),
    # path('auth/',include('rest_framework.urls',namespace='auth'))
]
