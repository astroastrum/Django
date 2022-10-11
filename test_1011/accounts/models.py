from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User에 들어가는 필드는?
# User Model은 이미 존재했다. 어디서? sqlite의 auth_user
# auth_user 앱 이름_모델 이름
# user 모델을 가지고 와서 사용 = 클래스 상속
# 장고 내부에 있는 데이터를 가져와서 migrate 진행함
# AbstractUser는 AbstractBaseUser를 상속받고 있다

class User(AbstractUser):
  # 별도의 설정 없음
  pass

# 상속 구조 이유
# models.Model > class AbstractBaseUser > class AbstractUser > class User
# 비밀번호 인증은 여러 설정이 들어가야 하는데 만들기 보다는 고민 없이 사용할 수 있도록 한다
# username은 AbstractUser에서 정의해놓음
# 그래서 비밀번호 인증 기능만 필요하면 AbstractBaseUser를 상속받으면 된다
