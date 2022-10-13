from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

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

@login_required
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
    


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST일 경우, input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, detail 페이지로
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면, context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET일 경우, Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)



def delete(request, pk):
  
  Article.objects.get(id=pk).delete()

  return redirect('articles:index')