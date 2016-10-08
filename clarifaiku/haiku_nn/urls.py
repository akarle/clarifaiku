from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^add_from_files$', views.add_from_files, name='add_from_files'),
]