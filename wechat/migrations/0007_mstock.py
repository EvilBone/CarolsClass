# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0006_auto_20171103_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='MStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='股票代码')),
                ('stock_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='股票名称')),
                ('stock_cprice', models.CharField(blank=True, max_length=50, null=True, verbose_name='当前价格')),
                ('stock_lprice', models.CharField(blank=True, max_length=50, null=True, verbose_name='昨收价格')),
                ('stock_followers_count', models.CharField(blank=True, max_length=50, null=True, verbose_name='关注人数')),
                ('stock_mprice', models.CharField(blank=True, max_length=50, null=True, verbose_name='最高价格')),
                ('stock_low_price', models.CharField(blank=True, max_length=50, null=True, verbose_name='最低价格')),
                ('stock_amount_qty', models.CharField(blank=True, max_length=50, null=True, verbose_name='成交量')),
                ('stock_amount_moneny', models.CharField(blank=True, max_length=50, null=True, verbose_name='成交额')),
                ('stock_desc', models.TextField(blank=True, null=True, verbose_name='简介')),
                ('stock_business', models.CharField(blank=True, max_length=50, null=True, verbose_name='业务')),
                ('stock_pbv', models.CharField(blank=True, max_length=50, null=True, verbose_name='市盈率')),
                ('stock_pe', models.CharField(blank=True, max_length=50, null=True, verbose_name='市净率')),
                ('stock_profit', models.CharField(blank=True, max_length=50, null=True, verbose_name='每股收益')),
                ('stock_assets', models.CharField(blank=True, max_length=50, null=True, verbose_name='每股资产')),
                ('stock_dividend', models.CharField(blank=True, max_length=50, null=True, verbose_name='每股股息')),
            ],
        ),
    ]