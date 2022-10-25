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
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    # 사용자가 입력한 값을 활용해야함
    # 값을 어떤 이름으로 활용해야 하는지 작성
    # 사용자는 사용자의 이름을 작성한다
    path('welcome/<name>/', views.welcome),
    path('fake/', views.fake, name='fake'),
    path('fakenaver/', views.fakenaver, name='fakenaver'),
    path('accounts/', include('accounts.urls')),
]
