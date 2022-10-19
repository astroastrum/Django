from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  # 사용자가 작성한 모든 글을 DB에서 가져오기
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


# 중요
# ModelForm 활용
def new(request):
  form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)


def create(request):
  # DB에 저장
  # 1. parameter로 날라온 데이터를 받아서
  # request GET에서 content 파라키터로 날라온 데이터를 잡아서 content에 넣으려고 한다
  title = request.POST.get('title')
  content = request.POST.get('content')
  # DB에 저장
  # 2. 데이터가 저장됨
  article = Article.objects.create(title=title, content=content)
  
  return redirect('articles:detail', article.pk)
  
  # article.pk 오류
  # return redirect('articles:detail', article.pk)
  


def detail(request, pk):
  # 특정 pk의 데이터를 불러온다
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)


# detail 페이지에 작성
def delete(request, pk):
  # 특정 pk의 데이터를 불러온다
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')


# detail 페이지에 edit 페이지로 이동하는 링크를 작성한다
# edit 페이지로 이동하면 사용자가 다시 글을 작성할 수 있는 form이 주어진다
# 작성한 글을 제출하면 update에서 db에 저장한다
# db에 저장되면 실제로 edit한 글이 update된다
def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/edit.html', context)


# edit.html에 <form action="{% url 'articles:update' article.pk %}" method="POST">
def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  # update을 하면 detail 페이지로 이동
  return redirect('articles:detail', article.pk)






