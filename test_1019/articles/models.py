from django.db import models

# 모델에 정의한 필드의 종류와 구성에 따라 HTML Form이 정해짐
# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)