from django.db import models
import django_tables2 as tables


# Create your models here.

class Task(models.Model):
    PRI_CHOICES = (
        (1, u'紧急重要'),
        (2, u'紧急不重要'),
        (3, u'重要不紧急'),
        (4, u'不重要不紧急'),
    )
    TYPE_CHOICES = (
        (1, u'需求管理'),
        (2, u'日常工作'),
        (3, u'数据核对'),
        (4, u'功能验证'),
        (5, u'流程梳理'),
        (6, u'流程梳理'),
        (7, u'其他'),
    )
    PROGRESS_CHOIES = (
        (1, u'未开始'),
        (2, u'需求调研'),
        (3, u'用例整理'),
        (4, u'文档编写'),
        (5, u'文档完成'),
        (6, u'待确认'),
        (7, u'确认完成'),
        (8, u'待开发'),
        (9, u'开发中'),
        (10, u'开发完成'),
        (11, u'需求验证'),
        (12, u'用户验收'),
        (13, u'待上线'),
        (14, u'发布上线'),
        (15, u'已完成'),
        (16, u'处理中'),
    )
    tname = models.CharField(max_length=500, verbose_name='任务')
    priority = models.IntegerField(verbose_name='优先级', choices=PRI_CHOICES)
    description = models.TextField(verbose_name='描述')
    type = models.IntegerField(verbose_name='类型', choices=TYPE_CHOICES)
    progress = models.IntegerField(verbose_name='进度', default=0)
    checkperson = models.CharField(max_length=20, verbose_name='检查人')
    requestperson = models.CharField(max_length=20, verbose_name='提出人')
    transactor = models.CharField(max_length=20, verbose_name='执行人')
    planstartdate = models.DateField(verbose_name='计划开始日期')
    realstartdate = models.DateField(verbose_name='实际开始日期', blank=True, null=True)
    planenddate = models.DateField(verbose_name='计划完成日期')
    realenddate = models.DateField(verbose_name='实际完成日期', blank=True, null=True)
    relativeperson = models.CharField(max_length=200, verbose_name='关联人')
    analysis = models.TextField(verbose_name='任务分析', blank=True, null=True)
    currentobstacles = models.TextField(verbose_name='当前障碍', blank=True, null=True)
    summary = models.TextField(verbose_name='总结', blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', choices=PROGRESS_CHOIES, default=1)

    class Meta:
        verbose_name_plural = '任务'
        verbose_name = '任务'

    def row_style(self):
        if self.priority == 1:
            return 'danger'
        elif self.priority == 2:
            return 'warning'
        elif self.priority == 3:
            return 'success'
        else:
            return 'info'


class TaskTable(tables.Table):
    class Meta:
        model = Task
        template = 'django_tables2/bootstrap.html'
        row_attrs = {
            'class': lambda record: record.row_style(),
            'id': lambda record: record.pk
        }
        attrs = {'class': 'table table-hover table-condensed tasktable table-bordered'}
        fields = (
        'id', 'tname', 'priority', 'type', 'status', 'requestperson', 'transactor', 'checkperson', 'planstartdate',
        'realstartdate', 'planenddate', 'realenddate', 'relativeperson')
