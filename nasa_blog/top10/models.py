
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Top10(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    header = RichTextField(null=False, blank=False)
    content = RichTextField(null=True, blank=True)
    year = models.IntegerField(null=False, blank=False, default=2000)
    image = models.ImageField(upload_to='top10', null=True, blank=True)
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

    class Meta:
        unique_together = (
            "title",
            "year",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Noticia: {self.title}, {self.year}"

