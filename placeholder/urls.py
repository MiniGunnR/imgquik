from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^image/(?P<width>\d+)/$', views.placeholder_shortcut, name='placeholder_shortcut'),
    url(r'^image/(?P<width>\d+)x(?P<height>\d+)/$', views.placeholder, name='placeholder'),
    url(r'^image/(?P<width>\d+)x(?P<height>\d+)/(?P<bg>\w+)/$', views.placeholder, name='placeholder_bg'),
    url(r'^image/(?P<width>\d+)x(?P<height>\d+)/(?P<bg>\w+)/(?P<fg>\w+)/$', views.placeholder, name='placeholder_bg_fg'),
    url(r'^$', views.index, name='homepage'),
]
