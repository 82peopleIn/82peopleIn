from django.urls import path
from chu import views

app_name = 'chu'

urlpatterns = [
    path('', views.chu_list, name='chu_list'),
    path('<int:pk>/', views.chu_detail, name='chu_detail'),
]
