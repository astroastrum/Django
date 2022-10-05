from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
  fields = ['title', 'created_at', 'updated_at']

# admin 사이트에 Article 등록
admin.site.register(Article, ArticleAdmin)
