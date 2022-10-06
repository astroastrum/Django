from django.db import models

# Create your models here.
# 1. class 모델 설계 (DB의 스키마 설계)
class Article(models.Model):
  # 스키마 설계 (데이터베이스 테이블)
  title = models.CharField(max_length=20)
  summary = models.TextField()
  running_time = models.DateTimeField(auto_now_add=True)

