from django.conf.urls import  include, url
from .views import wechat

urlpatterns = [
  url(r'^$', wechat,name='wechat'),
]