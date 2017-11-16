from django.contrib import admin

# Register your models here.
from timertask.models import MTask, MSche, MScheLog




class MScheInline(admin.StackedInline):
    model = MSche

class MTaskAdmin(admin.ModelAdmin):
    list_display = ('task_name','task_desc','task_createtime')

    inlines = [MScheInline, ]


class MScheAdmin(admin.ModelAdmin):
    list_display = ('task','sche_excute_time','sche_isacive','sche_status')

class MScheLogAdmin(admin.ModelAdmin):
    list_display = ('ms_task','ms_start_time','ms_end_time')

admin.site.register(MTask, MTaskAdmin)
admin.site.register(MSche, MScheAdmin)
admin.site.register(MScheLog, MScheLogAdmin)