from django.urls import path
from . import views

urlpatterns = [
    path('room_list', views.room_list, name='main_room_list'),
    path('', views.root, name='root')
]
