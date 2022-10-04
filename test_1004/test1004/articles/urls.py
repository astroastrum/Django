# URL 설정을 app 단위로 하기 위해서
from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
  # '로컬호스트의 articles로 들어오면 어떠한 페이지를 처리하겠다'는 계획을 세운다
  # 여기에 views의 index라고 하는 함수를 실행할 것이며 이를 index라고 부르겠다
  # http://127.0.0.1:8000/articles/
  path('index/', views.index, name='index'),
  # http://127.0.0.1:8000/articles/new/
  path('new/', views.new, name='new'),
  # http://127.0.0.1:8000/articles/create/
  path('create/', views.create, name='create'),
]