from django.conf.urls import url

from content import views

urlpatterns = [
    url(r'^$', views.lesson_list, name='lesson_list'),
    url(r'^(?P<lesson_id>\d+)/$', views.detail, name='detail'),
]