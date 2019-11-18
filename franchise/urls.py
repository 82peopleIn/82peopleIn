from django.urls import path, include
from franchise import views

app_name = 'franchise'

urlpatterns = [
    # 프랜차이즈
    path('', views.franchise_list, name='franchise_list'),
    # path('<int:pk>/', views.franchise_detail, name='franchise_detail'),
    path('juicy/', views.juicy, name='juicy'),
    path('gongcha/', views.gongcha, name='gongcha'),
    path('subway/', views.subway, name='subway'),
    path('momstouch/', views.momstouch, name='momstouch'),
    path('starbucks/', views.starbucks, name='starbucks'),
    path('ediya/', views.ediya, name='ediya'),
    path('sinjeon/', views.sinjeon, name='sinjeon'),
    path('caffebene/', views.caffebene, name='caffebene'),
    path('mrsd/', views.mrsd, name='mrsd'),
    path('gs25/', views.gs25, name='gs25'),
    path('cu/', views.cu, name='cu'),
    path('bhc/', views.bhc, name='bhc'),
    path('baek/', views.baek, name='baek'),
    path('tous/', views.tous, name='tous'),

]