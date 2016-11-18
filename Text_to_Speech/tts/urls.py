from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createmp3/', TemplateView.as_view(template_name='tts/createmp3.html')),
]