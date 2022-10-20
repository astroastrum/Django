from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from imagekit.processors import ResizeToFill

# 모델에 정의한 필드의 종류와 구성에 따라 HTML Form이 정해짐
# Create your models here.

from django.conf import settings 

class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = ProcessedImageField(
    blank=True, 
    processors=[Thumbnail(200,300)],
    format='JPEG',
    options={'quality': 90},  
    )

  def __str__(self):
    return self.title



class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.content