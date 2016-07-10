
from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^encode$', views.Encode.as_view(), name='encode'),
            url(r'^decode$', views.Decode.as_view(), name='decode'),
            ]
