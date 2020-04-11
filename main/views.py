from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room
from .forms import CreateRoomForm


def root(req):
    return redirect('main_room_list')


def room_list(req):

    # 방 목록 가져오기 / 게임 중인 방은 아래
    rooms = Room.objects.all().order_by('-status')

    return render(req, 'main/room_list.html', {'rooms': rooms})


@login_required
def room_create(req):

    if req.method == 'POST':
        create_room_form = CreateRoomForm(req.POST)

        if create_room_form.is_valid():
            room_instance = create_room_form.save(commit=False)

            room_instance.host = req.user

            room_instance.save()

            # 방이 제대로 만들어졌다면
            return redirect('main_room_list')

    else:
        create_room_form = CreateRoomForm()

    return render(req, 'main/room_create.html', {'form': create_room_form})
