from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # 사용자가 작성한 모든 글을 DB에서 가져오기
    articles = Article.objects.all()
    context = {
      'articles': articles
    }
    return render(request, 'articles/index.html', context)

'''
# before new + create 
# 중요
# ModelForm 활용
'''
def new(request):
  form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)



'''
ModelForm 활용전 create 함수

def create(request):
  # DB에 저장
  # 1. parameter로 날라온 데이터를 받아서
  # request GET에서 content 파라키터로 날라온 데이터를 잡아서 content에 넣으려고 한다
  title = request.POST.get('title')
  content = request.POST.get('content')
  # DB에 저장
  # 2. 데이터가 저장됨
  article = Article.objects.create(title=title, content=content)
  
  return redirect('articles:detail', article.pk)
  
  # article.pk 오류
  # return redirect('articles:detail', article.pk)
'''

''' 
before new + create
# ModelForm 활용 후 create 함수의 변화


def create(request):
  # 유효성 검사
  if request.user.is_authenticated:
    if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
    else:
      article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)
  else:
    return redirect('accounts:login')
'''

@login_required
def create(request):
    if request.method == 'POST':
      article_form = ArticleForm(request.POST)
      # article_form이 유효한지 검사
      if article_form.is_valid():
          article_form.save()
          return redirect('articles:index')
    else: # 유효하지 않다면
        article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
  
    return render(request, 'articles/form.html', context=context)




'''
# after new + create
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
          article = form.save()
          return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()
    context = {
      'form': form,
    }
    return render(request, 'articles/create.html', context)
'''

 


def detail(request, pk):
  # 특정 pk의 데이터를 불러온다
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/detail.html', context)



# detail 페이지에 작성
def delete(request, pk):
  # 특정 pk의 데이터를 불러온다
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')



'''
before edit + update
# detail 페이지에 edit 페이지로 이동하는 링크를 작성한다
# edit 페이지로 이동하면 사용자가 다시 글을 작성할 수 있는 form이 주어진다
# 작성한 글을 제출하면 update에서 db에 저장한다
# db에 저장되면 실제로 edit한 글이 update된다
'''
def edit(request, pk):
  article = Article.objects.get(pk=pk)
  form = ArticleForm(instance=article)
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/edit.html', context)






'''
ModelForm 활용 전 update 함수 

# edit.html에 <form action="{% url 'articles:update' article.pk %}" method="POST">
def update(request, pk):
  article = Article.objects.get(pk=pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  # update을 하면 detail 페이지로 이동
  return redirect('articles:detail', article.pk)

'''

'''
before edit + update
# ModelForm 활용한 UPDATE

def update(request, pk):
  article = Article.objects.get(pk=pk)
  form = ArticleForm(request.POST, instance=article)
  if form.is_valid():
    form.save()
    return redirect('articles:detail', article.pk)

  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/edit.html', context)
'''


'''
after edit + update

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
          form.save()
          return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)
    context = {
      'form': form,
      'article': article,
    }
    return render(request, 'articles/update.html', context)
'''


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)