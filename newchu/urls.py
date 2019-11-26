from django.urls import path
from newchu import views

app_name = 'chu222'

urlpatterns = [
    path('', views.index, name='new_chu'),
    # path('<int:pk>/', views.chu222_detail, name='chu222_detail'),
]
