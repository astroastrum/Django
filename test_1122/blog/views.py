from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  # DB에서 불러옴
  articles = Article.objects.all()
  context = {
    'articles': articles,
  }
  return render(request, 'blog/index.html', context)


def create(request):
    
    if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
          article_form.save()
          return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    
    return render(request, 'blog/form.html', context=context)


def detail(request, pk):
    # 특정 글을 가져온다 
    # 요청한 객체가 있으면 해당 객체를 리턴하고 없으면 404 처리
    article = get_object_or_404(Article, pk=pk)
    context = {
      'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    # 원래 기존에 작성한 글을 불러오기
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)