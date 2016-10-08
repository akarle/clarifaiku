from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Haiku(models.Model):
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    line1 = models.CharField(max_length=30)
    line2 = models.CharField(max_length=30)
    line3 = models.CharField(max_length=30)


class Theme(models.Model):
    theme = models.CharField(max_length=30)
