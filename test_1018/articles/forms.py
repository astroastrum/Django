from socket import fromshare
from django import forms 
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ['title', 'content', 'image']

# CommentForm을 넘겨주는 장고의 VIEW 함수는 detail
class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ['content',]