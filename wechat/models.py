from django.db import models

# Create your models here.

class Student(models.Model):
    stu_num = models.CharField(max_length=20)
    wechart_name = models.CharField(max_length=100)
    stu_name = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=20)
    stu_grade = models.CharField(max_length=20)

class MUser(models.Model):
    user_id = models.CharField(max_length=20,verbose_name='id')
    user_name = models.CharField(max_length=100,verbose_name='名称',default='',blank=True,null=True)
    user_description = models.TextField(max_length=500,verbose_name='描述',default='',blank=True,null=True)
    user_follower_counts = models.IntegerField(verbose_name='粉丝数')
    user_friends_count = models.IntegerField(verbose_name='关注数')
    user_gender = models.CharField(max_length=2,verbose_name='性别',blank=True,null=True,default='')
    user_province = models.CharField(max_length=20,verbose_name='省份',blank=True,null=True)
    user_stocks_count = models.IntegerField(verbose_name='股票数',blank=True,null=True,default=0)
    user_is_deal = models.BooleanField(verbose_name='是否处理',default=False)
    
class MArticle(models.Model):
    article_title = models.CharField(max_length=400,verbose_name='标题')
    article_content = models.TextField(verbose_name='内容')
    article_author = models.CharField(max_length=100,verbose_name='作者')
    article_author_id = models.CharField(max_length=20,verbose_name='作者id')
    article_url = models.URLField(verbose_name='文章地址')