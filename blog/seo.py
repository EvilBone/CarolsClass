from django.contrib.sitemaps import Sitemap
from blog.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(blog_status=2)

    def lastmod(self, obj):
        return obj.blog_datetime