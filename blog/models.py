from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='标签')

    class Meta:
        verbose_name_plural='标签'
        verbose_name='标签'
    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = (
        (1, u'草稿'),
        (2, u'发布'),
        (3, u'作废'),
    )
    blog_title = models.CharField(max_length=200,verbose_name='标题')
    blog_author = models.CharField(max_length=100,verbose_name='作者')
    blog_content = RichTextField(verbose_name='内容')
    blog_datetime = models.DateTimeField(verbose_name='更新时间',auto_now=True)
    blog_createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    blog_views = models.IntegerField(verbose_name='浏览次数',default=1  )
    blog_status = models.IntegerField(verbose_name='状态',default=1,choices=STATUS_CHOICES)
    blog_category = models.ManyToManyField(Category,verbose_name='标签')

    class Meta:
        verbose_name = '博文'
        verbose_name_plural='博文'

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客',on_delete=True)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=True)
    comment_ctime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    parent_comm = models.ForeignKey('self',verbose_name='父评论',default=1,on_delete=True)
    content = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural='评论'

