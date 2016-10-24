from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<key>[0-9]+)$', views.profile, name="profile"),
]
