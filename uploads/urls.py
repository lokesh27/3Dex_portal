from django.conf.urls import patterns, include, url
from .views import list,index
urlpatterns = patterns('',
    url(r'^$', list),
    url(r'^list/$', list, name='list'),
    )