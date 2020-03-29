from django.shortcuts import render, redirect
from .models import Room


def root(req):
    return redirect('main_room_list')


def room_list(req):

    rooms = Room.objects.all()

    return render(req, 'main/room_list.html', {'rooms': rooms})

