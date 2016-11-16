from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from .forms import Mp3DetailsForm

def index(request):
    # print "We're here and the request is "
    template = None
    if request.method == 'POST':
        print ("This is a post request" + request.method)
        print(request)


        form = Mp3DetailsForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data['file_name'])
            print (form.cleaned_data['text'])
            template = loader.get_template('tts/createmp3.html')
            return HttpResponse(template.render(request))
        else:
            print(form)
            template = loader.get_template('tts/createmp3.html')
            return HttpResponse(template.render(request))
    else:
        form = Mp3DetailsForm()
        template = loader.get_template('tts/index.html')
        return HttpResponse(template.render(request))



# this part works sorta, not sure why i spent time doing that.
def createMP3(request):
    if request.method == 'POST':
        # template = loader.get_template('tts/createmp3.html')
        return HttpResponse("we handled the post")

    template = loader.get_template('tts/createmp3.html')
    return  HttpResponse(template.render(request))