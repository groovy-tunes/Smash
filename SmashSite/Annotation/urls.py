from django.conf.urls import url, include
from django.views.generic import ListView
from Annotation.models import Vod, Post
from . import views

urlpatterns = [
    url(r'^page(?P<page>[0-9+])$', views.vod, name="Annotation-feed"),
    url(r'^(?P<key>[0-9]+)$', views.post, name="Annotation-post"),
    url(r'^vote(?P<vkey>[0-9]+)/(?P<key>[0-9]+)$', views.vote, name="Annotation-vote"),
    url(r'^delete(?P<vkey>[0-9]+)/(?P<key>[0-9]+)$', views.delete, name="Annotation-delete"),    
    url(r'^deleteVod(?P<vkey>[0-9]+)', views.delete_vod, name="Annotation-delete-vod"),
    url(r'^Search(?P<search_text>.*)', views.search, name="Annotation-search")
    ]

