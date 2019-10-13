from django.conf.urls import url
from django.urls import path, include, re_path
from question import views

app_name = 'question'

urlpatterns = [
    # 공지사항
    path('', views.question_list, name='question_list'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('new/', views.question_new, name='question_new'),  # 등록
    path('remove/<int:pk>/', views.question_remove, name='question_remove'),  # 삭제
    path('edit/<int:pk>/', views.question_edit, name='question_edit'),  # 수정
    #

]