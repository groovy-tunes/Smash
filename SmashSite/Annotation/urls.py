from django.conf.urls import url, include
from django.views.generic import ListView
from Annotation.models import Vod, Post
from . import views

urlpatterns = [
    url(r'^$', views.vod, name="Annotation-feed"),
    url(r'^(?P<key>[0-9]+)$', views.post, name="Annotation-post"),
    url(r'^vote(?P<vkey>[0-9]+)/(?P<key>[0-9]+)$', views.vote, name="Annotation-vote")
    ]

