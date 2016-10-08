from django.shortcuts import render
from django.http import HttpResponse
import learn
from models import *
import os
from django.conf import settings
# Create your views here.



def index(request):
    add_from_files()
    return HttpResponse('test')



def addHaiku(theme, l1, l2, l3):
    m_theme, _ = Theme.objects.update_or_create(theme=theme)
    m_haiku = Haiku.objects.update_or_create(theme=m_theme, line1=l1, line2=l2, line3=l3)

def add_from_files():
    if not os.path.exists(settings.HAIKU_DIR):
        os.makedirs(settings.HAIKU_DIR)
    for theme in os.listdir(settings.HAIKU_DIR):
        for filename in os.listdir(os.path.join(settings.HAIKU_DIR, theme)):
            with open(os.path.join(settings.HAIKU_DIR, theme, filename)) as f:
                lines = [line for line in f.read().splitlines() if line and not line.isspace()]
                print lines
                for haiku_lists in [lines[i:i + 3] for i in range(0, len(lines), 3)]:
                    addHaiku(theme, haiku_lists[0],haiku_lists[1],haiku_lists[2])
