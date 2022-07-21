from django.db import models
from django.contrib.auth import models as auth_models
from django.conf import settings


# Create your models here.
class employee(auth_models.AbstractUser):
    name = models.CharField(max_length=25)
    mail = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    add = models.CharField(max_length=50,blank=True)
    gender_choices = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=gender_choices,default='M')
    
    def __str__(self) -> str:
        return f"{self.id} {self.name}"    
