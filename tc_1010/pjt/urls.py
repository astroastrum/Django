"""pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from practices import views as practices_views
# from articles import views as articles_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', practices_views.index),
    # path('ping/', practices_views.ping),
    # path('pong/', practices_views.pong),
    
    # 빈칸은 로컬호스트
    # path('', articles_views.index),
    path('articles/', include('articles.urls')),
    path('practices/', include('practices.urls')),
]
