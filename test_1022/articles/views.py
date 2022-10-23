from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  # DB에서 가져오기
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


def create(request):
  if request.method == 'POST':
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