from django.conf.urls import include, url
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from django.contrib.sitemaps import views as sitemaps_views
from blog.models import Blog
from blog.views import index, blog, add_comment, account_profile, reading

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name='blog'),
    url(r'^(?P<blog_id>[0-9]+)', blog, name='blog'),
    url(r'^addcoment/',add_comment,name='add_comment'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^accounts/profile/$', account_profile, name='account_profile'),
    url(r'^reading',reading,name='reading')

]