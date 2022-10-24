from django import forms
from .models import Article

# ModelForm class 상속받음
class ArticleForm(forms.ModelForm):
  class Meta:
    # 어떤 모델을 기반으로 form을 만들것인가
    model = Article
    fields = ['title', 'content', 'image']