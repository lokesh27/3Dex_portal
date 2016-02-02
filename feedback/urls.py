from django.conf.urls import url,include
from views import send_form
urlpatterns=[
    url(r'^send/', send_form),
]