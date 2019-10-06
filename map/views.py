
from django.shortcuts import render

from map.models import Gu

#
# def index(request):
#     return render(request, 'map/map_index.html')

def gu_list(request):
    qs = Gu.objects.all()
    return render(request, 'map/map_index.html',
                  {'gu_list': qs})