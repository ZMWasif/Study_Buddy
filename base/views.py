from django.shortcuts import render
from .models import Room

# Create your views here.

""" rooms = [
    {"id": 1, "name": "Lets learn Django"},
    {"id": 2, "name": "Lets learn Python"},
    {"id": 3, "name": "Lets learn JavaScript"},
    {"id": 4, "name": "Lets learn React"},
    {"id": 5, "name": "Lets learn Angular"},
    {"id": 6, "name": "Lets learn Vue"},
    {"id": 7, "name": "Lets learn Node"},
    {"id": 8, "name": "Lets learn Express"},
] """


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)
