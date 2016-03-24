from django.conf.urls import url,include
from discussions import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^ask/', views.ask),
]