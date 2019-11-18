from chartit import DataPool, Chart
from django.shortcuts import render, get_object_or_404


# Create your views here.
from chu.models import Chu

def chu_list(request):
    chus = Chu.objects.all()

    return render(request, 'chu/chu_list.html', {
        'chu_list': chus })

def chu_detail(request, pk):
    chus = get_object_or_404(Chu, pk=pk)

    context = {
        'chu': chus,
    }
    return render(request, 'chu/chu_detail.html',
                  context)
