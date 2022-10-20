from django.contrib import admin
from django.contrib.auth.admin import admin
from .models import User

# Register your models here.
admin.site.register(User)
