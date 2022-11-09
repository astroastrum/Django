from django.shortcuts import render, redirect, get_object_or_404

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
    # 사용자가 입력한 값을 받는다
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("reviews:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }
    return render(request, "accounts/signup.html", context)

def index(request):
    members = get_user_model().objects.all()
    return render(request, "accounts/index.html")

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



def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        forms = CustomUserChangeForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        forms = CustomUserChangeForm(instance=request.user)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/update.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        forms = PasswordChangeForm(request.user, request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:detail")
    else:
        forms = PasswordChangeForm(request.user)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/change_password.html", context)


def detail(request, user_pk):
    person = get_user_model()
    person = get_object_or_404(person, pk=user_pk)
    context = {
        "person": person,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def follow(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        return redirect("accounts:detail", user_pk)
    else:
        return HttpResponseForbidden()


@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:login")


@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = ProfileForm(instance=request.user)
    return render(
        request,
        "accounts/profile_update.html",
        {
            "form": form,
        },
    )
