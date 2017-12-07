from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm
from .models import User

class ComContentForm(forms.Form):
    com_content = forms.CharField(widget=CKEditorWidget())

class UserDetailForm(ModelForm):
    class Meta:
       # 关联的数据库模型，这里是用户模型
        model = User
       # 前端显示、可以修改的字段
        fields = ('username','avatar',)