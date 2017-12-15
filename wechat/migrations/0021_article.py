# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0020_auto_20171117_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='标题')),
                ('des', models.TextField(verbose_name='描述')),
                ('picurl', models.URLField(verbose_name='图片链接')),
                ('url', models.URLField(verbose_name='文章链接')),
            ],
        ),
    ]
