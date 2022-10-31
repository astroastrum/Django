from django.shortcuts import render

app_name = 'accounts'
# Create your views here.
def signup(request):
  return render(request, 'accounts/signup.html')
