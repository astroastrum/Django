from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
  # DB에서 가져오기
  articles = Article.objects.all()
  context = {
    'articles': articles,
  }
  return render(request, 'articles/index.html', context)


def new(request):
  return render(request, 'articles/new.html')


def create(request):
  # content라는 이름으로 request안에 담겨있는 get안의 content라고 하는 것을 사용할것이다
  # request GET에서 content 파라미터로 날라온 데이터를 잡아서 content(변수명)에 넣으려고 한다
  title = request.GET.get('title')
  content = request.GET.get('content')
  # DB에 저장
  # Article아 record 하나 만들게
  article = Article.objects.create(title=title, content=content)
  article.save()
  return redirect('articles:index')