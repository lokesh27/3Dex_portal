"""portal_3dex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
import portal_3dex.views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^content/', include('content.urls'),name='content'),
    url(r'^$', portal_3dex.views.do_login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^auth/$', portal_3dex.views.auth_view),
    url(r'^feedback/', include('feedback.urls'),name='feedback'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
