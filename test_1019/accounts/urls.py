from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('<int:pk>/', views.detail, name='detail'),
  path('logout/', views.logout, name='logout'),
  path('', views.index, name='index'),
  path('update/', views.update, name='update'),
  path('password/', views.change_password, name='change_password'),
]