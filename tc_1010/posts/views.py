from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# 첫번째 read는 index
def index(request):
  # 모든 (사용자가 작성한)글 목록을 보여준다
  # 1. DB에서 모든 글을 불러온다
  posts = Post.objects.all()
  # 2. template에 보내준다
  context = {
    'posts': posts,
  }
  return render(request, 'posts/index.html', context)


# 두번째 read는 하나의 데이터에 대한 정보를 출력
def detail(request, pk_):
  # 17번 글이면 17번 글을 불러와서 detail page에 전달해야한다
  # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다
  # pk를 index.html에서 가져와야한다
  # 불러온 데이터를 변수에 할당
  post = Post.objects.get(pk = pk_)
  # template에서 이 값들을 사용하기 위해 render에 인자로 넘겨준다
  context = {
    'post': post,
  }    
  return render(request, 'posts/detail.html', context)


# posts/new.html에 posts를 반드시 작성해야함
def new(request):
  return render(request, 'posts/new.html')


def edit(request, pk_):
  # get 메소드 사용해서 특정 pk를 불러온다
  # read
  post = Post.objects.get(pk = pk_)
  context = {
    "post": post,
  }
  return render(request, 'posts/edit.html', context)


def create(request):
  # DB에 저장
  # 1. parameter로 날라온 데이터를 받아서 
  title = request.GET.get('title')
  content = request.GET.get('content')


  # 2. DB에 저장
  # title, content를 가져왔고 DB에도 title=날라온 데이터
  # 데이터가 저장됨
  Post.objects.create(title=title, content=content)

  context = {
    'title': title,
    'content': content,
  }
  # return render(request, 'posts/create.html', context)
  return redirect('posts:index')


def update(request, pk_):
  # update할 특정 데이터를 가져온다
  post = Post.objects.get(pk = pk_)
  title_ = request.GET.get('title')
  content_ = request.GET.get('content')

  # 데이터를 수정
  post.title = title_ 
  post.content = content_
  # 데이터를 수정한 것을 반영
  post.save()
  # 데이터의 detail 페이지로 redirect
  return redirect('posts:detail', post.pk)



def delete(request, pk):
  # pk에 해당하는 글 삭제
  # id에는 pk를 넣을것이다
  Post.objects.get(id=pk).delete()
  # 삭제는 페이지를 보여주는 것이 아니라 해당 글을 삭제하는 것
  return redirect('posts:index')
