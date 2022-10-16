from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
  # 모든 (사용자가 작성한)글 목록을 보여준다
  # 1. DB에서 모든 글을 불러온다
  posts = Post.objects.all()
  # 2. template에 보내준다
  context = {
    'posts': posts,
  }
  return render(request, 'posts/index.html', context)


def new(request):
  return render(request, 'posts/new.html')


def create(request):
  # DB에 저장
  # 1. 데이터 받기
  title = request.GET.get('title')
  content = request.GET.get('content')

  # 2. 데이터 저장
  Post.objects.create(title=title, content=content)

  context = {
    'title': title,
    'content': content,
  }
  return redirect('posts:index')


def delete(request, pk):
  # pk에 해당하는 글 삭제
  # 삭제할 특정 데이터를 불러오고 삭제한다
  Post.objects.get(id=pk).delete()
  # 삭제는 페이지를 보여주는 것이 아니라 해당 글을 삭제하는 것
  return render('posts/index')


def detail(request, pk_):
  # 특정 pk의 데이터를 불러온다
  post = Post.objects.get(pk = pk_)
  context = {
    'post': post,
  }
  return render(request, 'posts/detail.html', context)