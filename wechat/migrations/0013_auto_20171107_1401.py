# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0012_auto_20171107_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mstock',
            name='stock_symbol',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='股票编码'),
        ),
    ]
