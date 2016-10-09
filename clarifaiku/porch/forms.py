from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='Enter a url', max_length=100)
