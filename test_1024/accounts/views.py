from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
# 프로필
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):
  # POST 요청 처리
  # request의 method가 POST라면 회원가입 처리를 해줘야 하고
  if request.method == 'POST':
    # 유효성 검사
    # 사용자가 입력한 값을(request.POST) form에 넣음
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
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
      return redirect(request.GET.get('next') or 'articles:index')
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
    # user = get_user_model().objects.get(pk=pk)
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        return redirect("accounts:login")


@login_required
def update(request):
    form = CustomUserChangeForm(instance=request.user)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
      form = CustomUserChangeForm(instance=request.user)
 
    context = {
        "form": form
        }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:detail", request.user.id)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)


# 팔로우 기능
# 사용자 프로필 페이지에 들어가서,
# 팔로우를 누르면 추가 (add)
# (이미) 팔로우 상태이면,
# 팔로우 취소 버튼을 누르면 삭제 (remove)


# 팔로우 상태가 아니면, 팔로우를 누르면 추가 (add)
# (이미) 팔로우 상태이면, 팔로우 취소 버튼을 누르면 삭제 (remove)

@login_required
def follow(request, pk):
  # 프로필에 해당하는 유저를 로그인한 유저가
  # 팔로우 상태가 아니면, 팔로우를 누르면 추가 (add)
  # user = get_user_model().objects.get(pk=user_pk)
  user = get_object_or_404(get_user_model(), pk=pk)
  if request.user == user:
    messages.warning(request, 'self follow not allowed')
    return redirect('accounts:detail', pk)
  if request.user in user.followers.all():
  # (이미) 팔로우 상태이면, 팔로우 취소 버튼을 누르면 삭제 (remove)
    user.followers.remove(request.user)
  else:
  # 팔로우 상태가 아니면, '팔로우'를 누르면 추가
    user.followers.add(request.user)
  return redirect('accounts:detail', pk)










'''
@login_required
def follow(request, user_pk):
  if request.user.is_authenticated:
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person != request.user:
    # 팔로우 상태가 아니면, '팔로우'를 누르면 추가(add)
    # user는 항상 get_user_model에서 
      if person.followers.filter(pk=request.user.pk).exits():
        person.followers.remove(request.user)
      # user = get_user_model().objects.get(pk=user_pk)
      # if request.user in user.followers.all():
      # 프로필에 해당하는 유저를 로그인한 유저가
      # user.followings.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:detail', user_pk)
  return redirect('accounts:login')
'''




'''
or

@login_required
def follow(request, pk):
    # 팔로우 상태가 아니면, '팔로우'를 누르면 추가(add)
    # user는 항상 get_user_model에서 
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다')
        return redirect('accounts:detail', pk)
        if request.user in user.followers.all():
        # 프로필에 해당하는 유저를 로그인한 유저가
            user.followings.add(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:detail', pk)


'''

