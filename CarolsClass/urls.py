"""CarolsClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.views.decorators.cache import cache_page

from CarolsClass import settings
from blog import views
from django.contrib.sitemaps import views as sitemaps_views

from blog.models import Blog

sitemaps = {
    'blog': GenericSitemap({'queryset': Blog.objects.filter(blog_status=2), 'date_field': 'blog_datetime'},
                           priority=0.6),
    # 如果还要加其它的可以模仿上面的
}
urlpatterns = [
                  url(r'^$', views.index),
                  url(r'^admin/', admin.site.urls),
                  url(r'^wechat/', include('wechat.urls')),
                  url(r'^blog/', include('blog.urls')),
                  url(r'^task/', include('taskmanager.urls')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                  url(r'^accounts/', include('allauth.urls')),
                  url(r'^sitemap\.xml$',
                      cache_page(86400)(sitemaps_views.index),
                      {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
                  url(r'^sitemap-(?P<section>.+)\.xml$',
                      cache_page(86400)(sitemaps_views.sitemap),
                      {'sitemaps': sitemaps}, name='sitemaps'),
                  url(r'^tracking/', include('tracking.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
