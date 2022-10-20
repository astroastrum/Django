from django import forms
from .models import Article, Comment

# ModelForm class 상속받음
class ArticleForm(forms.ModelForm):
  # Meta class 선언
  class Meta:
    # 어떤 모델을 기반으로 form을 만들것인가
    model = Article
    fields = ['title', 'content', 'image']

class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ['article', 'user']
    