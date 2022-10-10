from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
  # 모든 글 목록을 보여준다
  # 1. DB에서 모든 글을 불러온다
  posts = Post.objects.all()
  # 2. template에 보내준다
  context = {
    'posts': posts,
  }
  return render(request, 'posts/index.html', context)

# posts/new.html에 posts를 반드시 작성해야함
def new(request):
  return render(request, 'posts/new.html')

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


def delete(request, pk):
  # pk에 해당하는 글 삭제
  # id에는 pk를 넣을것이다
  Post.objects.get(id=pk).delete()
  # 삭제는 페이지를 보여주는 것이 아니라 해당 글을 삭제하는 것
  return redirect('posts:index')
