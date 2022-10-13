from django.urls import path
from . import views
# app_name 사용하는 이유
# 기본적으로 URL을 변수화해서 사용하고 있음
# Template, View에서 app_name과 path이름으로 진행
app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('update/', views.update, name='update'),
  # User 상세보기
  # integer로 pk를 받는다
  path('<int:pk>/', views.detail, name='detail'),
]