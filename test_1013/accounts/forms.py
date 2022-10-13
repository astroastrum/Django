# form을 상속받음

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
      # 내가 가지고 있는 User Model = models.py에 내가 상속받은 Model
      model = get_user_model()
      fields = ('username', )

# 또는
# fields = '__all__'

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'