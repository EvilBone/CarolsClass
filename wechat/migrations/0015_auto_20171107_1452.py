# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0014_mstock_stock_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='mstock',
            name='stock_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='涨跌幅'),
        ),
        migrations.AlterField(
            model_name='mstock',
            name='stock_change',
            field=models.FloatField(blank=True, null=True, verbose_name='涨跌额'),
        ),
    ]
