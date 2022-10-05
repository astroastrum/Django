from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)



def new(request):
  return render(request, 'articles/new.html')



'''
def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('articles:index')
'''

def create(request):
  if request.method == 'POST':
    
    # DB에 저장하는 로직
    article_form = ArticleForm(request.POST)
    if article_form.is_valid():
      article_form.save()
      return redirect('articles:index')
  else:
    article_form = ArticleForm()

  context = {
    'article_form': article_form
  }
  return render(request, 'articles/create.html', context=context)



def detail(request, pk):
  # 특정 글을 가져옴
  article = Article.objects.get(pk=pk)
  # template에 객체 전달
  context = {
    'article': article
  }
  return render(request, 'articles/detail.html', context)

'''
def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
'''