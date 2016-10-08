from django.shortcuts import render
from django.http import HttpResponse
import clarifaiku.haiku_nn.learn
from clarifaiku.haiku_nn.models import *
# Create your views here.



def index(request):
    return HttpResponse('test')


def addHaiku(theme, text):
    m_theme = Theme(theme=theme)
    m_theme.save()
    m_haiku = Haiku(theme=theme)

