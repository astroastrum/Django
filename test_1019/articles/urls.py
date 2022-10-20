from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  # new page: 글 작성/제출
  path('new/', views.new, name='new'),
  # create page: 작성한 글을 db에 저장
  path('create/', views.create, name='create'),
  # detail page: 작성한 글을 보여주는 목록
  path('<int:pk>/detail/', views.detail, name='detail'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  path('<int:pk>/edit/', views.edit, name='edit'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
