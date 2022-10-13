from django.shortcuts import render, redirect
# 인증과 관련된 곳에 UserCreationForm = 회원가입 form = user과 연결된 ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# detail에서 User 참조할 때 from .models import User 사용금지
# from .models import User 사용금지
from django.contrib.auth import get_user_model


# Create your views here.
# 3. CustomUserCreationForm 사용 (accounts에 정의한 User로 변경)
# settings.py의 기본 설정은 auth.User였는데 accounts.User로 변경했음
# 그래서 CustonUserCreationForm으로 변경
# 장고에 내제되어 있는 Form 사용
def signup(request):
    # POST 요청 처리
    # request의 method가 POST라면 회원가입 처리를 해줘야 하고
    if request.method == 'POST':
        # ModelForm로직의 기본
        # 유효성 검사
        # 사용자가 입력한 값을(request.POST) form에 넣음
        form = CustomUserCreationForm(request.POST)
        # 질문: valid한가? 
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    # GET 요청일 때
    # 나머지는, GET 요청일때는 Form을 UserCreationForm을 넣어서 
    else:
        form = CustomUserCreationForm()
    # signup.html에 {{ form.as_p }}로 사용함
    context = {
      'form': form
    }
    return render(request, 'accounts/signup.html', context)


'''
1. 회원가입 form 제공 기능

def signup(request):
  # 회원가입 form
  form = UserCreationForm()
  # signup.html에 {{ form.as_p }}로 사용함
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)
'''


'''
2. UserCreationForm 사용

def signup(request):
    # POST 요청 처리
    # request의 method가 POST라면 회원가입 처리를 해줘야 하고
    if request.method == 'POST':
        # ModelForm로직의 기본
        # 유효성 검사
        # 사용자가 입력한 값을(request.POST) form에 넣음
        form = UserCreationForm(request.POST)
        # 질문: valid한가? 
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    # GET 요청일 때
    # 나머지는, GET 요청일때는 Form을 UserCreationForm을 넣어서 
    else:
        form = UserCreationForm()
    # signup.html에 {{ form.as_p }}로 사용함
    context = {
      'form': form
    }
    return render(request, 'accounts/signup.html', context)


'''

# User class 참조하는 것만 다름
def detail(request, pk):
  # User 정보를 받아오는 쿼리셋 API 
  # User class 참조할 때 어떻게 작성? from .models import User가 아닌 from django.contrib.auth import get_user_model
  # user = User.objects.get(pk=pk), User가 아닌 get_user_model()
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
  }
  return render(request, 'accounts/detail.html', context)
