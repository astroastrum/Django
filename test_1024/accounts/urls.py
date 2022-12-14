from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  # path('', views.index, name='index'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('<int:pk>/', views.detail, name='detail'),
  path('update/', views.update, name='update'),
  path('delete/', views.delete, name='delete'),
  path('change_password/', views.change_password, name='change_password'),
  path('<int:user_pk>/follow/', views.follow, name='follow'),
]