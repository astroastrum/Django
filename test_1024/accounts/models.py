from django.db import models
from django.contrib.auth.models import AbstractUser
# 이미 내장되어 있는 모델 사용
# 모델에 있는 User는 Username, Firstname, Lastname, Email, Password 등의 필드를 가지고 있음
# User 모델을 Custom User Model로 대체함
# 맞춤설정을 위해서
# Create your models here.
class User(AbstractUser):
    pass