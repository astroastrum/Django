from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
  path("reviews/", views.index, name='index'), 
  path("reviews/create/", views.create, name='create'),
  path("reviews/<int:pk>/", views.detail, name='detail'),
  path("reviews/<int:pk>/update/", views.update, name='update'),
  path("reviews/<int:pk>/delete/", views.delete, name='delete'),
]
