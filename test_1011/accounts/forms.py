from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model

# 상속 받아서 내가 사용하고 있는 모델
# User 모델의 기본 내장 설정은 Auth 앱의 User Class
# AUTH_USER_MODEL은 프로젝트 중간에 사용하지 못한다. 그래서 초반에 사용해야함
# USER 모델을 대체하기 위해서는 
class CustomUserCreationForm(UserCreationForm):

    class Meta:
      model = get_user_model()
      fields = ('username', )

  
