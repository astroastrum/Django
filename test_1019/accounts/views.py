from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages


# Create your views here.
def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')

  else:
    form = CustomUserCreationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)


def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      # form.save()
      auth_login(request, form.get_user())
      if request.GET.get('next'):
        return redirect(request.GET.get('next'))
      else:
        return redirect('articles:index')   
      
  else:
    form = AuthenticationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/login.html', context)




# 프로필 페이지
def detail(request, pk):
  # User 정보를 불러와서 return render
  # User 정보를 받아오는 쿼리셋 API
  # from django.contrib.auth import get_user_model
  # 함수로 참조 (User Class를 참조)
  # User = get_user_model() 또는
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
  }
  return render(request, 'accounts/detail.html', context)


def index(request):
  return render(request, 'accounts/index.html')


def logout(request):
  auth_logout(request)
  messages.warning(request, '로그아웃 하였습니다.')
  return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)