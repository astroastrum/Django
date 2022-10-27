from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 모든 (사용자가 작성한)글 목록을 보여줌
    # 1. DB에서 모든 글을 불러옴
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)