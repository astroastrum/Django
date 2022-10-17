from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  # path('new/', views.new, name='new'),
  path('form/', views.form, name='form'),
  path('<int:pk>/', views.detail, name='detail'),
]