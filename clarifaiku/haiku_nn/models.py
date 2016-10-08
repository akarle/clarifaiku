from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Haiku(models.Model):
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    line1 = models.CharField(max_length=30)
    line2 = models.CharField(max_length=30)
    line3 = models.CharField(max_length=30)
    class Meta:
        unique_together = ('line1', 'line2', 'line3')

    def __str__(self):
        return '%s\n%s\n%s\n%s' %(self.theme, self.line1, self.line2, self.line3)
class Theme(models.Model):
    theme = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.theme