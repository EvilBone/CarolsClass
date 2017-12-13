import datetime

import pytz
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import localtime, utc
from imagekit.models import ProcessedImageField
# Create your models here.
from pilkit.processors import ResizeToFill


class User(AbstractUser):
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 #图片将处理成85x85的尺寸
                                 processors=[ResizeToFill(85,85)],)
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # 当用户更改头像的时候，avatar.name = '文件名'
        # 其他情况下avatar.name = 'upload_to/文件名'
        if len(self.avatar.name.split('/')) == 1:
            # print('before:%s' % self.avatar.name)
            # 用户上传图片时，将avatar.name改为 用户名/文件名
            self.avatar.name = self.username + '/' + self.avatar.name
        super(User, self).save()
        # 调用父类的save()方法后，avatar.name就变成了'upload_to/用户名/文件名'
        # print('after:%s' % self.avatar.name)
        # print('avatar_path: %s' % self.avatar.path)


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
    blog_abstract = RichTextUploadingField(verbose_name='摘要')
    blog_content = RichTextUploadingField(verbose_name='内容')
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

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def timeInternal(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        createtime = self.blog_createtime
        delta = (now-createtime).seconds
        ms = delta/60
        hours = ms/60
        days = (now-createtime).days
        mounths = days/30
        years = mounths/12
        if delta<60 and days==0:
            return '刚刚'
        elif ms<60 and days==0:
            return '%d分前'% ms
        elif hours<24 and days==0:
            return '%d小时前' % hours
        elif days<30:
            return '%d天前' % days
        elif mounths<12:
            return  '%d月前' % mounths
        else:
            return '%年前'% years

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='博客')
    user = models.ForeignKey(User,verbose_name='用户')
    comment_ctime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    parent_comm = models.ForeignKey('self',verbose_name='父评论',default=1)
    content = models.TextField(verbose_name='内容')

    def children(self):
        list = Comment.objects.filter(parent_comm=self)
        return list

    class Meta:
        verbose_name = '评论'
        verbose_name_plural='评论'


