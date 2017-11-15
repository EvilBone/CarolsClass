from django.shortcuts import render

# Create your views here.
from blog.models import Blog


def index(request):
    blogs = Blog.objects.order_by('-blog_createtime').all()
    return render(request, 'home.html', {'blogs': blogs})


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.blog_views += 1
    blog.save()
    return render(request, 'blog.html', {'blog': blog})
