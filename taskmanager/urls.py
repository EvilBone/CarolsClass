#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 11:15
# @Author  : Bone
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from taskmanager.views import task, edit_task, modify_task

app_name = 'taskmanager'

urlpatterns = [
    url(r'^$', task, name='task'),
    url(r'^edittask',edit_task, name='edit_task'),
    url(r'^(?P<id>[0-9]+)', modify_task, name='modify_task'),
]