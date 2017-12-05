from ckeditor.widgets import CKEditorWidget
from django import forms

class ComContentForm(forms.Form):
    com_content = forms.CharField(widget=CKEditorWidget())