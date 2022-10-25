from django.db import models


# Create your models here.
from django.conf import settings

class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  # 같은 모델을 참조하는 상황에서는 반드시 역참조 설정해야함
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  