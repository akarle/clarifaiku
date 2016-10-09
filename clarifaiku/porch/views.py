from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader

from .forms import UrlForm

import json

with open('key.json') as data_file:
    keys = json.load(data_file)


from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi(keys[0],keys[1])



# def index(request):
#     template = loader.get_template('porch/index.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

def get_url(request):
    # if this is a POST request we need to process the form data
    lines = []
    picture = "https://media-cdn.tripadvisor.com/media/photo-s/01/06/f7/e2/walden-in-autumn.jpg"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UrlForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/porch/response')
            picture = request.POST['url']
            result = clarifai_api.tag_image_urls(picture)

            for i in range(3):
                lines.append(result["results"][0]["result"]["tag"]['classes'][i])

            return render(request, 'porch/index.html', {'form': form, 'line1': lines[0],'line2': lines[1],'line3': lines[2], 'pic': picture})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UrlForm()
        lines = ["Here lies a haiku", "Original, it may seem","Refrigerator"]

    return render(request, 'porch/index.html', {'form': form, 'line1': lines[0],'line2': lines[1],'line3': lines[2], 'pic': picture})
