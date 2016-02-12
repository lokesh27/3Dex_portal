from django.conf.urls import url,include
from views import reg_form
urlpatterns=[
    url(r'^reg/', reg_form),
]