from django import forms
from .models import *

class SeoulForm(forms.ModelForm):
    class Meta:
        model = Seoul
        fields = ('name', 'sector', 'location', 'code', 'latitude', 'longitude')


class BucheonForm(forms.ModelForm):
    class Meta:
        model = Bucheon
        fields = ('name', 'sector', 'location', 'code', 'latitude', 'longitude')
