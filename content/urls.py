from django.conf.urls import url

from content import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<lesson_id>\d+)/$', views.detail, name='detail'),
]