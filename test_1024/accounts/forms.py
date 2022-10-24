from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User

class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model = get_user_model()
    fields = {'username', 'password'}


class CustomUserChangeForm(UserChangeForm):
  
  class Meta: 
    model = get_user_model()
    fields = '__all__'


