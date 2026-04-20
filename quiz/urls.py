from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.quiz_start, name='quiz_start'),
    path('play/', views.quiz_play, name='quiz_play'),
    path('result/', views.result, name='result'),
]