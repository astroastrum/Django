from socket import TIPC_CLUSTER_SCOPE
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# request = 요청 정보를 받는다
def index(request):
  # 게시글을 가져와서
  articles = Article.objects.all()
  # template에 전달한다
  context = {
    'articles': articles
  }
  # 원하는 페이지를 render한다
  return render(request, 'articles/index.html', context)


def new(request):
  return render(request, 'articles/new.html')



def create(request):
  # DB에 저장하는 로직
  # Parameter로 날라온 데이터를 받는다
  title = request.POST.get('title')
  
  # models.py의 Article
  # DB에 저장 (테이블에 저장)
  Article.objects.create(title=title)
  return render(request, 'articles/create.html')



def delete(request, article_pk):
  # 삭제해야 할 값을 불러온다
  articles = Article.objects.get(pk = article_pk)
  articles.delete()
  return redirect("articles:index")


# view에서 특정 pk값을 가지고 데이터를 불러와야 하기 때문에 pk값을 전달
# pk값을 받아야 한다 
def detail(request, pk_):
  # 글을 불러와서 template에 전달한다
  # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다
  # 내가 선택한 특정 글을 수정하기 위해서는 id가 필요하다
  # 불러온 데이터를 변수에 할당
  article = Article.objects.get(pk = pk_)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)
  # template에서 context의 값들을 변수로 사용하기 위해서 context 변수를 render에 인자로 넘겨준다


# URL에서 동적 인자를 전달해서 함수에서 동적 인자를 받아줘야 한다
def update(request, pk_):
  # update할 특정 데이터를 불러온다
  article = Article.objects.get(pk = pk_)
  title_ = request.GET.get('title')
  # 데이터 수정
  # 불러온 특정 데이터의 title을 내가 받아온 title로 바꾼다
  article.title = title_
  # 데이터 수정한 것을 반영
  article.save()
  
  # 내가 불러온 article의 pk 값 입력
  return redirect('articles:detail', article.pk)
  # edit 페이지에서 다른 글을 작성하고 제출하면 변경된 내용이 detail 페이지에 추가된다