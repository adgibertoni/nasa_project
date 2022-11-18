from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    header = RichTextField(null=False, blank=False)
    content = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

 