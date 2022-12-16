from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (
    login as user_login,
    logout as user_logout,
)

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            user = forms.save()
            user_login(request, user)
            return redirect("places:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        id = request.POST.get("id")
        password = request.POST.get("password")
        if form.is_valid():
            user_login(request, form.get_user())
            
            context = { "id": id, "password": password }
            return redirect(request.GET.get("next") or "places:index", context)
    else:
        form = AuthenticationForm()
    context = {"forms": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    user_logout(request)
    return redirect("places:index")