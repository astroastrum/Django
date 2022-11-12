from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  articles = Article.objects.all()
  context = {
    'articles': articles,
  }
  return render(request, 'articles/index.html', context)


def create(request):
  return render(request, "articles/create.html")


@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user 
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)