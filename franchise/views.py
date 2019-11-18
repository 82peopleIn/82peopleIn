from .models import Juicy, Gongcha, Subway, Starbucks, Momstouch, Ediya, Sinjeon, Caffebene, Mrsd
from django.shortcuts import get_object_or_404, render, redirect
from chartit import DataPool, Chart, PivotDataPool, PivotChart

# Create your views here.

def franchise_list(request):
    return render(request, 'franchise/franchise_list.html')

def juicy(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Juicy},
            'terms': [{'year': 'year',
                       'count': 'count'}],
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(239, 62, 54)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/JUICY.html', {'chart_list': [cht]})

def gongcha(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Gongcha},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(195, 32, 49)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/GONGCHA.html', {'chart_list': [cht]})

def subway(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Subway},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(0, 137, 57)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/SUBWAY.html', {'chart_list': [cht]})

def starbucks(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Starbucks},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(1, 119, 84)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/STARBUCKS.html', {'chart_list': [cht]})

def momstouch(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Momstouch},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(237, 37, 66)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/MOMSTOUCH.html', {'chart_list': [cht]})


def ediya(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Ediya},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(19, 35, 93)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/EDIYA.html', {'chart_list': [cht]})


def sinjeon(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Sinjeon},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(214, 21, 24)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/SINJEON.html', {'chart_list': [cht]})

def caffebene(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Caffebene},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(112, 90, 77)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/CAFFEBENE.html', {'chart_list': [cht]})

def mrsd(request):
    count = DataPool(
        series=
        [{'options': {
            'source': Mrsd},
            'terms': [{'year': 'year',
                       'count': 'count'}]
        },
        ])
    cht = Chart(
        datasource = count,
        series_options =
            [{'options': {
                'type': 'line',
                'stacking': False,
                'color': 'rgb(238, 48, 42)'},
               'terms':{
                  'year': [
                      'count']
            }}],
        chart_options =
        {'title': {
            'text': '연도별 가맹점 수'},
         'xAxis': {
             'title' : {'text': '연도'}},
         'yAxis': {
             'title': {'text': '가맹점 수'}}})
    return render(request, 'shop_name/MRSD.html', {'chart_list': [cht]})


def baek(request):
    return render(request, 'shop_name/baek.html')

def tous(request):
    return render(request, 'shop_name/tous.html')

def cu(request):
    return render(request, 'shop_name/cu.html')

def gs25(request):
    return render(request, 'shop_name/gs25.html')

def bhc(request):
    return render(request, 'shop_name/bhc.html')