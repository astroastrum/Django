from django import forms
from .models import Article


# ModelForm 선언 (대체 기능)
# 선언된 모델에 따른 필드 구성
# 1. Form 생성  2. 유효성 검사 
class ArticleForm(forms.ModelForm):
  
  class Meta:
    model = Article
    # 선언된 모델에 따른 필드들
    fields = ['title', 'content']