from django.db import models

# Create your models here.
'''
기능 기획
UI(User Interface)와 DB는 밀접한 관계
어떠한 서비스를 제공할 것인가
ex) 
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜와 시간)
'''

# 1. class 모델 설계 (DB의 스키마를 설계)
class Article(models.Model):
    # 스키마 설계 (데이터베이스 테이블)
    title = models.CharField(max_length=20)
    content = models.TextField()
    # add, 생성될 때 자동으로 기록
    create_at = models.DateTimeField(auto_now_add=True)
    # 그냥 자동으로 기록
    updated_at = models.DateTimeField(auto_now=True)