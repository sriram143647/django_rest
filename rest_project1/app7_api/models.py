from django.db import models

# Create your models here.
class student_detail(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=25)
    mail = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
    
class class_detail(models.Model):
    room_no = models.IntegerField()
    teacher_name = models.CharField(max_length=25)
    class_room = models.IntegerField()
    std_data = models.ForeignKey(student_detail,on_delete=models.CASCADE,related_name='std_detail')
    
    def __str__(self):
        return self.teacher_name