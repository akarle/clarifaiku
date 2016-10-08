from django.shortcuts import render
from django.http import HttpResponse
import learn
from models import *
import os
from django.conf import settings
# Create your views here.



def index(request):
    return HttpResponse('test')

def add_from_files(request):
    learn.add_from_files()
    return HttpResponse("Added haiku from files to database")



