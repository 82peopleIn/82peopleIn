from django.conf.urls import url
from django.urls import path
from map import views
from .views import *

app_name = 'map'

urlpatterns = [
    path('', views.index, name='map_index'),
    url(r'^seoul$', display_seoul, name="display_seoul"),
    url(r'^bucheon$', display_bucheon, name="display_bucheon"),
]
