from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('', views.gu_list, name='map_index'),
]
