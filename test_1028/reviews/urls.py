from django.urls import path
from . import views

app_name='reviews'

urlpatterns=[
  path('', views.index, name='index'),
  path('reviews', views.reviews, name='reviews'),
  path('create/', views.create, name='create'),
  path('<int:pk>/', views.detail, name='detail'),
]