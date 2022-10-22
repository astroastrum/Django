from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
  # DB에서 가져오기
  articles = Article.objects.all()
  context = {
    'articles': articles
  }
  return render(request, 'articles/index.html', context)