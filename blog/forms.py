from ckeditor.widgets import CKEditorWidget
from django import forms

class ComContentForm(forms.Form):
    blog_id = forms.IntegerField()
    com_content = forms.CharField(widget=CKEditorWidget())