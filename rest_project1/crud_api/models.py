from django.db import models

# Create your models here.
class student_data(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=25)
    mail = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    add1 = models.CharField(max_length=50,blank=True)
    add2 = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=10)
    
    def __str__(self):
            return self.name