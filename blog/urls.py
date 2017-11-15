from django.conf.urls import include, url
from .views import index, blog

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^blog/(P<blog_id>[0-9]+)/', blog, name='blog')
]