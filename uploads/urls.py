from django.conf.urls import url
from .views import list
from django.views.generic import TemplateView

urlpatterns=[
    url(r'^$', list),
    #url(r'^list/$', list.as_view()),
    url(r'^list/$', list,name='list')
]