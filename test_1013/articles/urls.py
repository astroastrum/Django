from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY
from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new, name='new'),
  path('create/', views.create, name='create'),
  path('delete/<int:pk>', views.delete, name='delete'),
  path('detail/<int:pk_>', views.detail, name='detail'),
  path('edit/<int:pk_>', views.edit, name='edit'),
  path('update/<int:pk_>', views.update, name='update'),
]