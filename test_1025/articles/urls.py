from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  # URL과 함수를 매핑한다
  # articles/URL과 views.py 파일의 index함수를 매핑한다
  path('', views.index, name='index'),
  
]