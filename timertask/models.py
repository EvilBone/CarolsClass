from django.db import models

# Create your models here.

class MTask(models.Model):
    task_name = models.CharField(max_length=100,verbose_name='任务名')
    task_desc = models.CharField(max_length=200,verbose_name='任务描述')
    task_createtime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = "任务"

class MSche(models.Model):
    STATUS = (
        ('W', 'waiting'),
        ('R', 'running'),
        ('S', 'stop'),
        ('F', 'finish'),
    )
    task = models.ForeignKey(MTask,on_delete=True)
    sche_excute_time = models.TimeField(verbose_name='运行时间')
    sche_isacive = models.BooleanField(verbose_name='是否启用', default=True)
    sche_status = models.CharField(max_length=20,verbose_name='状态',default='waiting')

    def __str__(self):
        return self.task.task_name+','+ self.sche_excute_time.strftime('%H:%M:%S')

    class Meta:
        verbose_name = '执行计划'
        verbose_name_plural = '执行计划'

class MScheLog(models.Model):
    ms_task = models.ForeignKey(MTask,on_delete=True)
    ms_start_time = models.DateTimeField(verbose_name='开始时间')
    ms_end_time = models.DateTimeField(verbose_name='结束时间')
    ms_message = models.TextField(verbose_name='日志内容')

    class Meta:
        verbose_name = '执行日志'
        verbose_name_plural = '执行日志'