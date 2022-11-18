from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField
# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    header = RichTextField(null=False, blank=False)
    content = RichTextField(null=True, blank=True)
    owner_new = models.ForeignKey (User, on_delete=models.CASCADE, default=5)
    comments_new = models.ManyToManyField(
        User, through="CommentNew", related_name="comments_new_owned"
    )
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

    class Meta:
        unique_together = (
            "title",
            "header",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Noticia: {self.title}, subida por {self.owner_new}"


class CommentNew(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    owner_new = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
