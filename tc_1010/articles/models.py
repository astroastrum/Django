from django.db import models

# 작성한 글을 영구적인 저장소에 넣는 방법
# 사용자가 작성했던 글이 있으면 무조건 저장을 해야함
# 저장을 한다는 것은 영구적인 저장소에 넣는다는 것 
# Create your models here.
# Object-relational mapping은 관계형 데이터베이스 테이블을 object, 객체로 만든다는 것이다
# 객체와 비슷한 테이블을 만들어야함
# 장고가 지원하는 ORM
# models에 들어있는 Model을 상속받는다
class Article(models.Model):
  # content라는 column을 넣어서 관리
  # 그리고 이것을 TextField라고 정의함
  content = models.TextField()

# 구조도에서 실제 DB로 만들기 위해서는 
# python manage.py makemigrations (설계도로 만듬)
# python manage.py migrate (실제 DB로 만듬)