"""testpjt URL Configuration

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
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # index/ 주문이 들어오면 articles app에 들어있는 views.py의 index함수가 핸들링 하게하라
    # 즉, 주문 들어오면 일단 index 함수에 보낸다.
    path('welcome/<name>/', views.welcome),
    # 꺽쇄(<>)는 주문서의 이름에 따라서 무언가를 하는 페이지 
]
