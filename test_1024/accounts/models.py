from django.db import models
from django.contrib.auth.models import AbstractUser
# 이미 내장되어 있는 모델 사용
# 모델에 있는 User는 Username, Firstname, Lastname, Email, Password 등의 필드를 가지고 있음
# User 모델을 Custom User Model로 대체함
# 맞춤설정을 위해서
# Create your models here.
class User(AbstractUser):
    # 장고는 ManyToManyField를 사용해서 자동으로 중개 테이블 생성
    # A가 B를 팔로잉, 서로 친구가 아님(symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'

# 팔로우 기능
# 사용자 프로필 페이지에 들어가서,
# 팔로우를 누르면 추가
# (이미) 팔로우 상태이면,
# 팔로우 취소 버튼을 누르면 삭제