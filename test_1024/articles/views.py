from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# request = HTTP 요청 객체
'''
def index(request):
  return HttpResponse("Hello World")
'''

# 함수 실행 결과를 웹 브라우저에 전달
def index(request):
    # 모든 (사용자가 작성한)글 목록을 보여줌
    # 1. DB에서 모든 글을 불러옴
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context)

'''
def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return render(request, 'articles/create.html')
'''

'''
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')
'''

'''
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
'''

def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:create')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # 특정 pk의 데이터를 불러온다
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
        'article': article,
    }
    return render(request, 'articles/new.html', context)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    # 삭제할 특정 데이터를 불러오고 삭제
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return render('articles:detail', pk)