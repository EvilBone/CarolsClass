from django.contrib import admin

# Register your models here.
from blog.models import Blog


class BloagAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_author','blog_createtime','blog_views','blog_status')
    list_filter = ('blog_status',)


admin.site.register(Blog,BloagAdmin)