from django import forms
from .models import Article

# DB 필드를 HTML Form으로 변화시키고 그 HTML Form에서 받는 데이터를 유효성 검사
# ModelForm은 선언된 모델에 따른 필드 구성을 한다
# ModelForm은 유효성 검사를 한다
# ModelForm을 활용해서 HTML Form을 제공한다

# 모델 form에 instance를 넘겨서 new.html의 form을 대체한다
# template에 무언가를 넘기기 위해 context를 넘긴다 
class ArticleForm(forms.ModelForm):

  class Meta:
    # Article model에 있는 (어떠한 DB의)
    model = Article
    # 모든 필드를 내가 가져다가 사용하겠다 (어떠한 필드)
    fields = '__all__'
    # fields = ['title', 'content']

# DB 필드를 HTML Form으로 변화시키고 그 HTML Form에서 받는 데이터를 유효성 검사


'''
사용자 input 값을 받아서 (request.POST)
유효성 검사를 하고
검사 통과하면
저장한다

article_form = ArticleForm(request.POST)
if article_form.is_valid()
article_form.save()
return redirect('articles:index')

'''