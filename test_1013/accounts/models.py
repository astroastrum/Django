from django.db import models
# AbstractUser를 상속받겠다
from django.contrib.auth.models import AbstractUser
# 모델 변경 = DB 변경
# 사용자의 정보가 필요할 경우 모델 필드 추가
# 모델을 직접 정의하는 것이 아니라 장고 내부의 것을 가져와서 사용


# 사용자 관리 위해서 무엇을 만들어야 하는가?
# DB 필요
# 모델 정의를 해야함. 어떻게? class User
# Create your models here.
# User에 들어가는 필드는?
# User 모델은 이미 auth_user에 존재했음
# auth = 앱 이름, user = 모델 이름
# 직접 사용하기 위해서 이 모델을 가져와야함
# 어떻게? Class 상속
# 장고에는 기본 모델이 있는데 모델을 Custom User Model로 대체해서 활용함
# 장고에 있는 User Model을 그대로 사용하는 것이 아니라 
# Custom User Model로 대체해서 활용할 것이다
# 모델을 변경한다는 것은 'DB를 변경되었다'는 의미
# AbstractUser를 상속받음
# 프로젝트 시작할 때 설정
class User(AbstractUser):
  
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'
