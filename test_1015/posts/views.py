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
  return render(request)


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