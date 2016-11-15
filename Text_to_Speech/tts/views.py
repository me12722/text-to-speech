from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MP3


def index(request):
    template = loader.get_template('tts/index.html')
    return HttpResponse(template.render(request))

def createMP3(request, file_name, text):
    return  HttpResponse("form goes here")