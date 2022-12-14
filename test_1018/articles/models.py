from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  image = ProcessedImageField(upload_to='images/', blank=True,
                              processors=[ResizeToFill(1200, 960)],
                              format='JPEG',
                              options={'quality': 60})


class Comment(models.Model):
  content = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)