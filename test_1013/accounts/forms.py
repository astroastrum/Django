# form을 상속받음

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
      # 내가 가지고 있는 User Model = models.py에 내가 상속받은 Model
      model = User
      fields = ('username', )

# 또는
# fields = '__all__'