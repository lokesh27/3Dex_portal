from django.conf.urls import url,include
from views import *
urlpatterns=[
    url(r'^reg/', reg_form),
    url(r'^info/', info),
    url(r'^picture/',update_picture),
]