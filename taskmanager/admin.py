from django.contrib import admin

# Register your models here.
from taskmanager.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tname', 'priority', 'type', 'progress', 'requestperson', 'transactor', 'checkperson', 'planstartdate',
        'realstartdate', 'planenddate', 'realenddate', 'relativeperson', )


admin.site.register(Task, TaskAdmin)
