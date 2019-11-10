from chartit import DataPool, Chart
from django.shortcuts import render, get_object_or_404


# Create your views here.
from sang.models import Sang

def sang_list(request):
    sangs = Sang.objects.all()

    return render(request, 'sang/sang2.html', {
        'sang_list': sangs })

def sang_detail(request, pk):
    sangs = get_object_or_404(Sang, pk=pk)

    context = {
        'sang': sangs,
    }
    return render(request, 'sang/sang_detail.html',
                  context)


