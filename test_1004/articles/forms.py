from django import forms
from .models import Article

# 모델 form에 instance를 넘겨서 new.html의 form을 대체한다
# template에 무언가를 넘기기 위해 context를 넘긴다 
class ArticleForm(forms.ModelForm):

  class Meta:
    # Article model에 있는
    model = Article
    # 모든 필드를 내가 가져다가 사용하겠다
    fields = '__all__'
    # fields = ['title', 'content']