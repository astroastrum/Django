from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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
  article_form = ArticleForm()
  context = {
    'article_form': article_form
  }
  return render(request, 'articles/new.html', context=context)


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

  '''
  def create(request):
  # 데이터의 개수가 많아지면 많아질수록 request.POST의 개수도 많아진다
  # article_form은 ArticleForm에 request.POST를 넘기고 
  # 만약에 article_form이 유효한지 검사할 수 있다

  # 사용자의 input값을 받아서
  # article_form = ArticleForm(request.POST)
	if article_form.is_valid():
	article.form.save()
	else:
		print('유효하지 않습니다')
  return redirect('articles:index')
  

  또는 

  def create(request):
    # 사용자의 input값을 받아서
    article_form = ArticleForm(request.POST)
	  if article_form.is_valid():
	      article.form.save()
        return redirect('articles:index')
	  else:
        # 유효하지 않을 경우
		    context = {
            'article_form': article_form
        }
        return render(request, 'articles/new.html', context=context)
    
  
    두개의 함수를 합치기

    def new 주석 처리한 후

    def create(request):
      if request.method == 'POST':
          # DB에 저장하는 로직
          article_form = ArticleForm(request.POST)
	        if article_form.is_valid():
	            article.form.save()
              return redirect('articles:index')
	    else:
          article_form = ArticleForm()
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/new.html', context=context)

  index.html에서
  <a href="{% url 'articles:create' %}">글 쓰기</a>

  urls.py에서도 
  new 경로 주석처린


  '''