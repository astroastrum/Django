from django.shortcuts import render, redirect

from .forms import SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from .forms import CustomUserChangeForm, ProfileForm
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

def login(request):
    # 사용자가 입력한 데이터 가져오기
    if request.method == "POST":
        # 사용자가 입력한 값
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인 함수
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "reviews:index")
    else:
        form = AuthenticationForm()
    context = {"forms": form}
    return render(request, "accounts/login.html", context)
