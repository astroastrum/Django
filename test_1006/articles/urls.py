# URL 설정을 app 단위로 하겠다
from django.urls import path
from . import views

app_name = 'articles'

# localhost/articles로 들어오면 어떠한 페이지를 처리하겠다
# 요청과 응답
urlpatterns = [
  # view의 index 함수를 실행할 것이고 이를 index라고 부른다
  path('index/', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  # delete의 동적인자 사용
  # int 타입 자동으로 지정됨
  path('delete/<int:article_pk>', views.delete, name='delete'),
  # 사용자가 detail 주소로 요청하면
  # VIEW 함수(detail)를 응답한다
  path('detail/<int:pk_>', views.detail, name="detail"),
  path('edit/<int:pk_>', views.edit, name='edit'),
  path('update/<int:pk_>', views.update, name='update'),
]