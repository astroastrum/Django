from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class meta:
        model = Article
        fields = ['title', 'content']