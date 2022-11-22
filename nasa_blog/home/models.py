from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"About info OK"

