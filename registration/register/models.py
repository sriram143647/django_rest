from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=30,unique=True)
    phone = models.CharField(max_length=10)
    add = models.CharField(max_length=50,blank=True)
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    
    def __str__(self):
        return self.name
    
    