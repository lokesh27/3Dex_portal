from django.conf.urls import url,include
from discussions.views import index
urlpatterns=[
    url(r'^$', index),
]