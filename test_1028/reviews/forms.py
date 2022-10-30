from socket import fromshare
from django import forms
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
  class Meta:
    fields = [
      'title',
      'content',
    ]