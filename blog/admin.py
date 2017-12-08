from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from blog.models import Blog, Category, Comment, User

class BloagAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_author','blog_createtime','blog_views','blog_status')
    list_filter = ('blog_status',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','parent_comm_id','content')


admin.site.register(Blog,BloagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User, UserAdmin)