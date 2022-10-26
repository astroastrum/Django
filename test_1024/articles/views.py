from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.views.decorators.http import require_POST, require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.
# request = HTTP 요청 객체
'''
def index(request):
  return HttpResponse("Hello World")
'''

# 함수 실행 결과를 웹 브라우저에 전달
def index(request):
    # 모든 (사용자가 작성한)글 목록을 보여줌
    # 1. DB에서 모든 글을 불러옴
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

''''
def new(request):
    article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context)
'''

'''
def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  Article.objects.create(title=title, content=content)
  return render(request, 'articles/create.html')
'''

'''
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return render(request, 'articles/create.html')
'''

'''
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')
'''

# GET과 POST의 합
def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, '글 작성 완료')
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    # 글 작성하는 버튼 누르면 get으로 전달됨
    # 링크를 누르면 홈페이지로 넘어감
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    # 특정 pk의 데이터를 불러온다
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


# create(form) + update(값이 미리 들어가 있는 form)
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, '글 수정 완성')
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form,
        
        }
        return render(request, 'articles/form.html', context)
    else:
        messages.warning(request, '작성자만 수정 가능')
        return redirect('articles:detail', article.pk)

''''
def delete(request, pk):
    # pk에 해당하는 글 삭제
    # 삭제할 특정 데이터를 불러오고 삭제
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
'''

@login_required
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
    return JsonResponse(context) 



# 좋아요를 누르지 않았으면, 좋아요 누르면 추가
# 좋아요 누른 상태이면, 좋아요 취소 버튼을 누르면 삭제

@login_required
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # article에 좋아요 추가
        # article에 like_users에 add(request의 user다)
        article.like_users.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)

