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
    # 이미지 원본 필요 없으면 ProcessedImageField를 사용해서 이미지 사이즈 조절 가능
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 800)],
                                format='JPEG',
                                options={'quality': 80})

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)