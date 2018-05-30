# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20171216_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='tname',
            field=models.CharField(default=1, max_length=500, verbose_name='任务'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, '未开始'), (2, '需求调研'), (3, '用例整理'), (4, '文档编写'), (5, '文档完成'), (6, '待确认'), (7, '确认完成'), (8, '待开发'), (9, '开发中'), (10, '开发完成'), (11, '需求验证'), (12, '用户验收'), (13, '待上线'), (14, '发布上线'), (15, '已完成'), (16, '处理中')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.IntegerField(choices=[(1, '需求管理'), (2, '日常工作'), (3, '数据核对'), (4, '功能验证'), (5, '流程梳理'), (6, '流程梳理'), (7, '其他')], verbose_name='类型'),
        ),
    ]