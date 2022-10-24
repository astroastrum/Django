from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# 프로필
from django.contrib.auth import get_user_model



# Create your views here.
def signup(request):
  # POST 요청 처리
  # request의 method가 POST라면 회원가입 처리를 해줘야 하고
  if request.method == 'POST':
    # 유효성 검사
    # 사용자가 입력한 값을(request.POST) form에 넣음
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else: # GET 요청일 경우
    form = CustomUserCreationForm()
  # signup.html에 {{ form.as_p }}로 사용함
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)

def index(request):
  return render(request, 'accounts/index.html')



def login(request):
  if request.method == 'POST':
    # AuthenticationForm은 ModelForm이 아님
    # data의 argument로 request에 POST가 들어옴
    form = AuthenticationForm(request.POST, data=request.POST)
    # ModelForm이 아니라서 save() 없음
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('articles:index')
  else:
    # form처리 한다고 로그인 되는 것은 아니여서 로직을 추가해야함
    form = AuthenticationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/login.html', context)



def logout(request):
  auth_logout(request)
  messages.warning(request, "로그아웃")
  return redirect("accounts:index")



def detail(request, pk):
    # User 정보를 받아오는 쿼리셋 API
    # User class 참조할 때는 from django.contrib.auth import get_user_model
    # user = User.objects.get(pk=pk), User가 아닌 get_user_model()
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)