from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [ 
  path('index/', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('delete/<int:pk>', views.delete, name='delete'),
  # detail의 동적인자 사용
  path('detail/<int:pk_>', views.detail, name='detail'),
  path('edit/<int:pk_>', views.edit, name='edit'),
  path('update/<int:pk_>', views.update, name='update'), 
]