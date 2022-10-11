from django.shortcuts import render, redirect
# 인증과 관련된 곳에 forms에 UserCreationForm을 가지고 오면
# from django.contrib.auth.forms import UserCreationForm
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
      form.save()
      return redirect('articles:index')
  else: # GET 요청일때
      form = CustomUserCreationForm()
  # invaild한 상황이면 23번부터 코드 실행됨
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)
  # invalid한 시점의 form은 오류 메시지가 모두 담겨있는 form, UserCreationForm(request.POST)