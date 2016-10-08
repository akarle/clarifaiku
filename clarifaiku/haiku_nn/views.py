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
    l1, l2, l3 = text.split('\n')[0:2]
    m_haiku = Haiku(theme=theme, line1=l1, line2=l2, line3=l3)

