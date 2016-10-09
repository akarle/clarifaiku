from django.shortcuts import render
from django.http import HttpResponse
import learn
from models import *
import os
from django.conf import settings
#from . import RNN, skip_gram
from . import crawl
# Create your views here.


def index(request):
    return HttpResponse('test')

def add_from_files(request):
    learn.add_from_files()
    return HttpResponse("Added haiku from files to database")

def run_model(request):
    #RNN.run_model()
    #from . import generator
    #skip_gram.run_skip_gram()
    return HttpResponse(crawl.generate_similar_haiku(Haiku.objects.all()[0]))



