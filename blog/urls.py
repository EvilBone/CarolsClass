from django.conf.urls import include, url
from .views import index, blog, add_comment

urlpatterns = [
    url(r'^$', index, name='blog'),
    url(r'^(?P<blog_id>[0-9]+)/', blog, name='blog'),
    url(r'^addcoment/',add_comment,name='add_comment')
]