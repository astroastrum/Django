from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서
def index(request):
  # 게시글을 가져와서
  articles = Article.objects.all()
  # 정렬을 역순으로 바꾸고 싶으면 articles = Article.objects.order_by('-pk')
  # Template에 전달한다
  context = {
    'articles': articles
  }
  # 원하는 페이지를 render한다
  return render(request, 'articles/index.html', context)


def new(request):
  return render(request, 'articles/new.html')


def create(request):
  # 실제 DB에 저장하는 로직
  # GET에서 'title' 정보를 가져옴
  '''
  title = request.GET.get('title')
  content = request.GET.get('content')
  '''
  title = request.POST.get('title')
  content = request.POST.get('content')
  # models.py의 Article
  # DB에 저장
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')