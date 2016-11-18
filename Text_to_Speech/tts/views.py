from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from .forms import Mp3DetailsForm
from .models import MP3

def index(request):
    template = None
    aform = None
    if request.method == 'POST':
        context = RequestContext(request)
        aform = Mp3DetailsForm(request.POST)
        if aform.is_valid():
            file_name = aform.cleaned_data['file_name']
            text = aform.cleaned_data['text']
            aform.save()
            return render(request, 'tts/createmp3.html', {'file_name': file_name, 'text':text})
        else:
            aform = Mp3DetailsForm()

        return render(request, 'tts/createmp3.html')

    else:
        form = Mp3DetailsForm()
        context = RequestContext(request)
        return render(request, 'tts/index.html', {'form':form})

#the following function may not be necessary, woops
# in the follwing method make a call to the pk of MP3 and then print the details!
def createMP3(request):
    if request.method == 'GET':
        print("we are here!")
        print(request)
        return HttpResponse("we handled the Get! " )
    if request.method == 'POST':
        print("we are posting son")
        return HttpResponse("we handled the Get! ")

    template = loader.get_template('tts/createmp3.html')
    return  HttpResponse(template.render(request))
