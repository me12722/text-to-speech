from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
url(r'^$/[a-z]+/[A-Za-z]+', views.index, name='index'),
    url(r'^createmp3', views.createMP3, name='createMp3'),
]