from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models


# Create your models here.
from django.conf import settings


class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='images/', blank=True)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)