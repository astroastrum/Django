from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  articles = Article.objects.order_by('-pk')
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


def detail(request, pk_):
  article = Article.objects.get(pk = pk_)
  context = {
    'article': article,
  }    
  return render(request, 'articles/detail.html', context)



def new(request):
  return render(request, 'articles/new.html')


def edit(request, pk_):
  
  article = Article.objects.get(pk = pk_)
  context = {
    "article": article,
  }
  return render(request, 'articles/edit.html', context)


def create(request):
    if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      # article_form이 유효한지 검사
      if article_form.is_valid():
          article_form.save()
          return redirect('articles:index')
    else: # 유효하지 않다면
        article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
  
    return render(request, 'articles/form.html', context=context)


def update(request, pk_):
 
  article = Article.objects.get(pk = pk_)
  title_ = request.GET.get('title')
  content_ = request.GET.get('content')

  
  article.title = title_ 
  article.content = content_
  
  article.save()
  
  return redirect('articles:detail', article.pk)



def delete(request, pk):
  
  Article.objects.get(id=pk).delete()

  return redirect('articles:index')