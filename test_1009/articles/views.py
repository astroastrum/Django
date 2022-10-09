from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
  # 게시글을 가져와서 
  articles = Articles.objects.all()
  # template에 전달 (사용자가 작성한 글을 보여줌)
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


# 하나의 데이터데 대한 정보를 출력
# 내가 선택한 특정 글을 수정하기 위해서는 id가 필요하다
# 특정 pk값을 가지고 데이터를 불러와야 하기 때문에 pk값을 전달
# pk값을 받아야 한다
def detail(request, pk_):
  # 글을 불러와서 template에 전달
  # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다
  # 불러온 데이터를 변수에 할당
  articles = Articles.objects.get(pk = pk_)
  context = {
    'articles': articles,
  }
  return render(request, 'articles/detail.html', context)
  # template에서 context의 값들을 변수로 사용하기 위해서 context 변수를 render에 인자로 넘겨준다


def new(request):
  return render(request, 'articles/new.html')


def edit(request):
  articles = Articles.objects.get(pk = pk_)
  context = {
    "articles": articles,
  }
  return render(request, 'articles/edit.html', context)


def create(request):
  # DB에 저장하는 로직
  title = request.GET.get('title')
  content = request.GET.get('content')
  # DB에 저장(테이블에 저장)
  Articles.objects.create(title=title)
  Articles.objects.create(content=content)
  return redirect('articles:index')


# pk는 정수형이고 넘어온다
def delete(request, articles_pk):
  # pk에 해당하는 글 삭제
  '''articles = Articles.objects.get(id = articles_pk).delete()'''
  articles = Articles.objects.get(pk = articles_pk)
  articles.delete()
  return redirect("articles:index")






def update(request, pk_):
  articles = Articles.objects.get(pk = pk_)
  title_ = request.GET.get('title')
  # 데이터 수정
  # 불러온 특정 데이터의 title을 내가 받아온 title로 바꾼다
  articles.title = title_
  # 데이터 수정한 것을 반영
  articles.save()
  # 내가 불러온 articles의 pk값 입력
  return redirect('articles:detail', articles.pk)
  # edit 페이지에서 다른 글을 작성하고 제출하면 변경된 내용이 detail 페이지에 추가된다