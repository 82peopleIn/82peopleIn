from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'map/map_index.html')

def display_seoul(request):
    items = Seoul.objects.all()
    context = {
        'items': items,
        'header': 'Seoul',
    }
    return render(request, 'map/map_index.html', context)


def display_bucheon(request):
    items = Bucheon.objects.all()
    context = {
        'items': items,
        'header': 'Bucheon',
    }
    return render(request, 'map/map_index.html', context)
