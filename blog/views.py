from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import ComContentForm, UserDetailForm
# Create your views here.
from blog.models import Blog, Comment


def index(request):
    blogs = Blog.objects.order_by('-blog_createtime').filter(blog_status=2)
    return render(request, 'home.html', {'blogs': blogs})

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not request.user.is_superuser:
        blog.blog_views += 1
    blog.save()
    commentform = ComContentForm()
    comments = Comment.objects.filter(blog=blog).order_by('-comment_ctime')
    return render(request, 'blog.html', {'blog': blog,'commentform':commentform,'comments':comments})

def add_comment(request):
    if request.method =='POST':
        blog_id = request.POST.get('blog_id')
        content = request.POST.get('com_content')
        comm_id = request.POST.get('comm_id')
        print(comm_id)

        if content!=None or content!='':
            comments = Comment()
            comments.blog_id = blog_id
            comments.content = content
            comments.user = request.user
            comments.parent_comm_id = comm_id
            comments.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def account_profile(request):
    messages = []
    # post请求 表明是在修改用户资料
    if request.method == 'POST':
        # 使用getattr可以获得一个querydict，里面包含提交的内容
        #request_dic = getattr(request, 'POST')
        #print(request_dic)
        #print(request.FILES)
        form = UserDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.append('资料修改成功！')
    # 如果是get请求，则使用user生成表单
    form = UserDetailForm(instance=request.user)
    return render(request, 'account/user_detail.html', context={'form':form,
                                                                'messages':messages,})