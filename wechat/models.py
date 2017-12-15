
from django.db import models

# Create your models here.

class Student(models.Model):
    stu_num = models.CharField(max_length=20)
    wechart_name = models.CharField(max_length=100)
    stu_name = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=20)
    stu_grade = models.CharField(max_length=20)
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = "学生"

class Article(models.Model):
    title = models.CharField(max_length=500,verbose_name='标题')
    des = models.TextField(verbose_name='描述')
    picurl = models.URLField(verbose_name='图片链接')
    url = models.URLField(verbose_name='文章链接')



