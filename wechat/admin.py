from django.contrib import admin


# Register your models here.
from wechat.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','des','picurl','url')

admin.site.register(Article, ArticleAdmin)