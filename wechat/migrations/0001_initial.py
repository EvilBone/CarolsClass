# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=400, verbose_name='标题')),
                ('article_content', models.TextField(verbose_name='内容')),
                ('article_author', models.CharField(max_length=100, verbose_name='作者')),
                ('article_author_id', models.CharField(max_length=20, verbose_name='作者id')),
                ('article_url', models.URLField(verbose_name='文章地址')),
            ],
        ),
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, verbose_name='id')),
                ('user_name', models.CharField(max_length=100, verbose_name='名称')),
                ('user_description', models.TextField(max_length=500, verbose_name='描述')),
                ('user_follower_counts', models.IntegerField(verbose_name='粉丝数')),
                ('user_friends_count', models.IntegerField(verbose_name='关注数')),
                ('user_gender', models.CharField(max_length=2, verbose_name='性别')),
                ('user_province', models.CharField(max_length=20, verbose_name='省份')),
                ('user_stocks_count', models.IntegerField(verbose_name='股票数')),
                ('user_is_deal', models.BooleanField(default=False, verbose_name='是否处理')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.CharField(max_length=20)),
                ('wechart_name', models.CharField(max_length=100)),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_class', models.CharField(max_length=20)),
                ('stu_grade', models.CharField(max_length=20)),
            ],
        ),
    ]
