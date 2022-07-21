from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class employee(AbstractUser):
    name = models.CharField(max_length=25)
    mail = models.EmailField(max_length=30,unique=True)
    phone = models.CharField(max_length=10)
    add = models.CharField(max_length=50,blank=True)
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    
    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS= ['username','name','phone','gender']
    
    def __str__(self):
        return self.username
    
    