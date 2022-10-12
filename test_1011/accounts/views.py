from django.shortcuts import render, redirect
# from .models import User 사용금지
# 인증과 관련된 곳에 forms에 UserCreationForm을 가지고 오면
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
  # POST 요청 처리
  # 만약에 POST 요청이라면 ModelForm 로직에서 기본
  # 사용자가 입력한 값을 받아서 form에 넣어주고
  # form = UserCreationForm(request.POST)
  # (request.POST)는 사용자가 입력한 값
  # form is valid 한가?
  # 그렇다면 form.save()
  # POST 요청일때는 valid까지 실행됨
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('articles:index')
  else: # GET 요청일때
      form = CustomUserCreationForm()
  # invaild한 상황이면 23번부터 코드 실행됨
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)
  # invalid한 시점의 form은 오류 메시지가 모두 담겨있는 form, UserCreationForm(request.POST)

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


def login(request):
    if request.method == 'POST':
      # AuthenticationForm은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
        # 세션에 저장
        # login 함수는 request, user 객체를 인자로 받음
        # user 객체는 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
      form = AuthenticationForm()
    context = {
      'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('articles:index')