from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from django_tables2 import RequestConfig

from taskmanager.forms import TaskDetailForm
from taskmanager.models import Task, TaskTable


def task(request):
    if request.method == 'GET':
        try:
            filter = request.GET['filter']
            if filter =='current':
                tasks = Task.objects.exclude(status=15)
                table = TaskTable(tasks)
                RequestConfig(request).configure(table)
            elif filter == 'finished':
                tasks = Task.objects.filter(status=15)
                table = TaskTable(tasks)
                RequestConfig(request).configure(table)
            else:
                tasks = Task.objects.all()
                table = TaskTable(tasks)
                RequestConfig(request).configure(table)
        except MultiValueDictKeyError:
            filter = 'current'
            tasks = Task.objects.exclude(status=15)
            table = TaskTable(tasks)
            RequestConfig(request).configure(table)

    return render(request, 'task.html', {'table': table,'filter':filter})


def edit_task(request):
    if request.method == "GET":
        obj = TaskDetailForm()
        return render(request, "edittask.html", {'obj': obj})
    elif request.method == "POST":

        obj = TaskDetailForm(request.POST)
        if obj.is_valid():
            task, created = Task.objects.update_or_create(id=obj.cleaned_data['id'], defaults=obj.cleaned_data)
        return HttpResponseRedirect("/task/")

def modify_task(request, id,):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        obj = TaskDetailForm(instance=task)
        return render(request, "edittask.html", {'obj': obj})
    elif request.method == "POST":
        obj = TaskDetailForm(request.POST,instance=task)
        if obj.is_valid():
            task, created = Task.objects.update_or_create(id=obj.cleaned_data['id'], defaults=obj.cleaned_data)
        return HttpResponseRedirect("/task/")
