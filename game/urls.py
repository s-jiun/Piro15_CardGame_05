from django.contrib import admin
from django.urls import path, include
from . import views

app_name= 'game' 

urlpatterns = [
    path('info/<int:pk>', views.game_info, name='game_info' ),
    path('result/', views.game_result, name ='game_result'),
    path('podium/', views.game_podium, name='game_podium'),
]