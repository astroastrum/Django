from django.shortcuts import render

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

# 로그인 기능 
# django-allauth 사용하기
# pip install django-allauth
# 설치 후, settings.py에 반드시 등록