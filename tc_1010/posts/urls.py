from django.urls import path
from . import views

'''
C 메인: 게시글의 목록 / 게시글 상세ㄱ
R 작성: 글을 작성하는 페이지 / 작성 완료하는 페이지
U 수정: 글을 수정하는 페이지 / 수정 완료하는 페이지
D 삭제: 글 삭제 완료 페이지
'''

app_name = 'posts'

urlpatterns = [
  path('', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  # pk의 자료형은 int
  path('delete/<int:pk>', views.delete, name='delete'),
]