from django.db import models


# Create your models here.
from django.conf import settings

class Article(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  