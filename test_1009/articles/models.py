from django.db import models

# Create your models here.
class Articles(models.Model):
  # 스키마 설계 (데이터베이스 테이블)
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
