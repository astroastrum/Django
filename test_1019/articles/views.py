from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
  # 사용자가 작성한 모든 글을 DB에서 가져오기
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


def new(request):
  return render(request, 'articles/new.html')


def create(request):
  # DB에 저장
  # 1. parameter로 날라온 데이터를 받아서
  # request GET에서 content 파라키터로 날라온 데이터를 잡아서 content에 넣으려고 한다
  title = request.POST.get('title')
  content = request.POST.get('content')
  # DB에 저장
  # 2. 데이터가 저장됨
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
  


def detail(request, pk):
  # 특정 pk의 데이터를 불러온다
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)