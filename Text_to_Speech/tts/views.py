from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .forms import Mp3DetailsForm

from gtts import gTTS

import os
import time


def index(request):

    if request.method == 'POST':
        context = RequestContext(request)
        aform = Mp3DetailsForm(request.POST)

        if aform.is_valid():
            file_name = aform.cleaned_data['file_name'].replace(" ", "")
            text = aform.cleaned_data['text']
            create_sound(file_name, text)
            file_path = '/Users/ivanG/Documents/text_to_speech/Text_to_Speech/' + file_name + ".mp3"

            while not os.path.exists(file_path):
                time.sleep(1)
                if os.path.exists(file_path):
                    break;

            print("file about to be opened")
            fsock = open(file_path, 'r')
            response = HttpResponse(fsock, content_type='audio/mpeg')
            response['Content-Disposition'] = "attachment; filename=%s.mp3" % file_name
            return response

        else:
            aform = Mp3DetailsForm()

        return render(request, 'tts/createmp3.html')

    else:
        form = Mp3DetailsForm()
        context = RequestContext(request)
        return render(request, 'tts/index.html', {'form': form})


def create_sound(file_name, text):
    txt = text
    tts = gTTS(text=txt, lang='en')
    tts.save(file_name + ".mp3")
    return tts
