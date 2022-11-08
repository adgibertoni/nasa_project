from ckeditor.widgets import CKEditorWidget
from django import forms

from picture.models import Picture

class PictureForm(forms.ModelForm):
    title_name = forms.CharField(
        label="Título:",
        max_length=80,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingresar el título",
                "required": "True",
            }
        )
    )
    
    image = forms.ImageField()

    taken_by = forms.CharField(
        label="Tomada por:",
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese quién/qué tomó la imagen",
                "required": "True",
            }
        )
    )

    taken_date = forms.DateField(
        label="Tomado el:",
        required=False,
        widget=forms.DateInput(
            attrs={
                "placeholder": "yyyy-mm-dd",
                "required": "False",
            }
        )
    )    
    
    class Meta:
        model = Picture
        fields = ["title_name", "image", "taken_by", "taken_date"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
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