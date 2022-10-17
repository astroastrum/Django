from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm



# Create your views here.
def index(request):
  articles = Article.objects.order_by('-pk')
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)

# 장고에서 Form을 통해 파일을 받을 경우 2가지 설정 필요
# 1. HTML Form 자체에서 
# 2. VIEW에서 파일 별도로 ModelForm에 넣어서

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        # images 폴더에 이미지가 들어옴
        # 이미지를 서버에 받을 수 있게됨
        print(request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
          article_form = ArticleForm()
    context = {
        'article_form':article_form
    }
      
    return render(request, 'articles/form.html', context=context)


# def new(request):
 # return render(request)


def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article
  }
  return render(request, 'articles/detail.html', context)