from django.contrib import admin
from .models import Article, Image


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'content', 'views', 'publish_time')


admin.site.register(Article, ArticleAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'views', 'publish_time')


admin.site.register(Image, ImageAdmin)
