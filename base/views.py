from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
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
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q) )
    topics = Topic.objects.all()
    context = {"rooms": rooms, 'topics': topics}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {'form': form}
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"room": room}
    return render(request, "base/delete.html", {'object_name': room})