from django.shortcuts import render

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

# 로그인 기능 
# django-allauth 사용하기
# pip install django-allauth
# 설치 후, settings.py에 반드시 등록
# (console.developers.google.com)에 접속 > 새 프로젝트 생성 페이지로 이동


def login(request):
  return render(request, 'accounts/login.html')