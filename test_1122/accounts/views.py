from django.shortcuts import render

# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')

# 로그인 기능 
# django-allauth 사용하기
# pip install django-allauth