from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  # URL과 함수를 매핑한다
  # articles/URL과 views.py 파일의 index함수를 매핑한다
  path('', views.index, name='index'),
  # path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/comments/', views.comment_create, name='comment_create'),
  # path('<int:pk>/delete/', views.delete, name='delete'),
  path('<int:pk>/like/', views.like, name='like'),
]