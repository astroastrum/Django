from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
  articles = Article.objects.order_by('-pk')
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)


def detail(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  context = {
    'article': article,
    'comments': article.comment_set.all(),
    'comment_form': comment_form,
  }
  return render(request, 'articles/detail.html', context)


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

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글이 수정되었습니다.')
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)


def comment_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(comment-False)
    comment.article = article
    comment.save()
  return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('articles:detail', article_pk)