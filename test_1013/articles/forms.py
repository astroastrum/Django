from django import forms
from .models import Article

# 장고에 있는 ModelForm을 가져옴
# 장고에 있는 것을 가져옴
class ArticleForm(forms.ModelForm):

    # Form에 넣는것
    class Meta:
        # models의 Article을 가져옴
        model = Article
        # article중에서 title이랑 content만 가져옴
        fields = ['title', 'content']