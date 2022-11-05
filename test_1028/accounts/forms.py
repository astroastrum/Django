from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "image",
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
