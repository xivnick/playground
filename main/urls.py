from django.urls import path
from . import views

urlpatterns = [
    path('room/list/', views.room_list, name='main_room_list'),
    path('room/create/', views.room_create, name='main_room_create'),
    path('', views.root, name='root')
]
