from django.conf.urls import url,include
from views import reg_form,info
urlpatterns=[
    url(r'^reg/', reg_form),
    url(r'^info/', info)
]