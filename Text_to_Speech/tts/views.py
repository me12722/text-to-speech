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
            aform.file_name = aform.cleaned_data['file_name']
            aform.text = aform.cleaned_data['text']
            aform.save()

            # the exists but not in modelform, it exists in MP3 model!!!!
            # hopefully this will help pave the way to a productive friday!
            # :)!!!
            return render(request, 'tts/createmp3.html',None, {'form': aform})
        else:
            aform = Mp3DetailsForm()

        return render(request, 'tts/createmp3.html')

    else:
        form = Mp3DetailsForm()
        context = RequestContext(request)
        return render(request, 'tts/index.html', {'form':form})

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
