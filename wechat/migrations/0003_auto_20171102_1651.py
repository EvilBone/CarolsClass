# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0002_auto_20171102_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='user_description',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='描述'),
        ),
    ]