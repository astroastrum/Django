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
  image = ProcessedImageField(upload_to='images/', blank=True,
                              processors=[ResizeToFill(1200, 960)],
                              format='JPEG',
                              options={'quality':80})
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  

# 수업                                
# python manage.py shell_plus
# article 하나 가져오기
# a1 = Article.objects.all()[0]

# like user 가져오기
# u1 = User.objects.all()[0]

# article object 7번 글에 좋아요를 누른 사람이 sun이라고 하는 사람이 있고
# a1.like_users.add(u1)
# al.like_users.all()

# 'sun이라는 사람이 좋아요를 누른 글은 7번이다' 라고 저장되어 있음
# u1.like_artcles.all()  


