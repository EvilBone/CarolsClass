from django.db import models

# Create your models here.

class Student(models.Model):
    stu_num = models.CharField(max_length=20)
    wechart_name = models.CharField(max_length=100)
    stu_name = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=20)
    stu_grade = models.CharField(max_length=20)