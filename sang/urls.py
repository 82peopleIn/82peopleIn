from django.urls import path
from sang import views

app_name = 'sang'

urlpatterns = [
    path('', views.sang_list, name='sang2'),
    path('<int:pk>/', views.sang_detail, name='sang_detail'),

]
