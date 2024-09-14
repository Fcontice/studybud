from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Lets learn Django'},
#     {'id':2, 'name':'Python is the best'},
#     {'id':3, 'name':'Javascript is the future'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)  # This line retrieves the room with the id that matches the pk parameter.
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}

    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)