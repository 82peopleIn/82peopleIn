from django.urls import path
from newchu import views

app_name = 'newchu'

urlpatterns = [
    path('', views.index, name='new_chu'),
    path('<int:pk>/', views.newchu_detail, name='newchu_detail'),
]
