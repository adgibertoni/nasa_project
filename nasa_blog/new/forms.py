from ckeditor.widgets import CKEditorWidget
from django import forms

from new.models import New

class NewForm(forms.ModelForm):
    title = forms.CharField(
        label="Título:",
        max_length=70,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresar el título",
                "required": "True",
                "rows": 2,
                "style":"min-width: 80%",
            }
        )
    )
    
    header = forms.CharField(
        label="Subtítulo:",
        required=False,
        widget=CKEditorWidget(
            attrs={
                "placeholder": "Ingresar breve reseña",
                "required": "True",
            }
        ),
    )
    
    content = forms.CharField(
        label="Desarrollo:",
        required=False,
        widget=CKEditorWidget(),
    )
        
    class Meta:
        model = New
        fields = ["title", "header", "content"]

class CommentNewForm(forms.Form):
    commentnew_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario aquí.",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )