from django.urls import path
from sang import views

app_name = 'sang'

urlpatterns = [
    path('', views.sang2, name='sang2'),
    path('sang3', views.sang3, name='sang3'),
    path('sang4', views.sang4, name='sang4'),
    path('sang5', views.sang4, name='sang5'),

]
