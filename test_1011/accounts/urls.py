from django.urls import path
from . import views

# app_name 사용하는 이유
# URL을 기본적으로 변수화해서 사용하고 있다
app_name = 'accounts'

urlpatterns = [
  # 회원가입 기능
   path('signup/', views.signup, name='signup'),
   # 프로필 페이지
   path('<int:pk>/', views.detail, name='detail'),
]