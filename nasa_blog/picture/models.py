from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

class Picture(models.Model):
    title_name = models.CharField(max_length=80, null=False, blank=False)
    image = models.ImageField(upload_to='picture', null=False, blank=False)
    taken_by = models.CharField(max_length=60, null=True, blank=True)
    taken_date = models.DateField()
    owner = models.ForeignKey (User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "title_name",
            "taken_by",
        )
        ordering = ["-taken_date"]

    def __str__(self):
        return f"Imagen {self.title_name}, tomada por {self.taken_by}"

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

