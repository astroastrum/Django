from django.urls import path
from . import views

# 동일한 index가 존재(practices에)할 경우 어떤 앱의 index(url 변수명)인지 구별할 수 있다
app_name = 'articles'

urlpatterns = [
  # 링크를 부를때 index라고 부름
  # name은 url을 변수화한것 = 여러변 활용할 때 변수를 사용
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
]