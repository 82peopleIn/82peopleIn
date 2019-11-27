from django.shortcuts import render, get_object_or_404

from newchu.models import Maechul


def index(request):
    return render(request, 'newchu/chu_list.html')
#
# def
#
# def mcScore(self):

def newchu_detail(request, pk):
    chu = get_object_or_404(Maechul, pk=pk)

    return render(request, 'newchu/chu_detail.html',
                  {'chu': chu})
