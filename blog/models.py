from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=200,verbose_name='标题')
    blog_author = models.CharField(max_length=100,verbose_name='作者')
    blog_content = RichTextField(verbose_name='内容')
    blog_datetime = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    blog_createtime = models.DateTimeField(verbose_name='创建时间',auto_now=True,auto_created=True)
    blog_views = models.IntegerField(verbose_name='浏览次数',default=0)

    class Meta:
        verbose_name = '博文'
        verbose_name_plural='博文'
