from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
  path('index/', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('delete/<int:pk>', views.delete, name='delete'),
  path('detail/<int:pk_>', views.detail, name='detail'),
]