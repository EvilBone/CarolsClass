from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import ComContentForm
# Create your views here.
from blog.models import Blog, Comment


def index(request):
    blogs = Blog.objects.order_by('-blog_createtime').filter(blog_status=2)
    return render(request, 'home.html', {'blogs': blogs})

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.blog_views += 1
    blog.save()
    commentform = ComContentForm()
    comments = Comment.objects.filter(blog=blog).order_by('-comment_ctime')
    return render(request, 'blog.html', {'blog': blog,'commentform':commentform,'comments':comments})

def add_comment(request):
    if request.method =='POST':
        blog_id = request.POST.get('blog_id')
        content = request.POST.get('com_content')
        if content!=None or content!='':
            comments = Comment()
            comments.blog_id = blog_id
            comments.content = content
            comments.user = request.user
            comments.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

