from django.contrib import admin

from .models import Article, comment

admin.site.register(Article)
admin.site.register(comment)

