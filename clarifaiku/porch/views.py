from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader

from .forms import NameForm

import json

with open('key.json') as data_file:
    keys = json.load(data_file)


from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi(keys[0],keys[1])



def index(request):
    template = loader.get_template('porch/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/porch/response')
            print request.POST['your_name']
            result = clarifai_api.tag_image_urls(request.POST['your_name'])

            for tag in result["results"][0]["result"]["tag"]['classes']:
                print tag

            return render(request, 'porch/name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'porch/name.html', {'form': form})
