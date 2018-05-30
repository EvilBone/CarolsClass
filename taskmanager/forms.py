from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from django.forms import ModelForm
from .models import Task


class TaskDetailForm(ModelForm):
    id = forms.IntegerField(required=False,widget=forms.HiddenInput())

    class Meta:
        # 关联的数据库模型，这里是用户模型
        model = Task
        # 前端显示、可以修改的字段
        fields = ('id','tname', 'priority', 'description', 'type', 'checkperson', 'requestperson', 'transactor', 'planstartdate',
        'planenddate','id')
