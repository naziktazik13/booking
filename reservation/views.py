from django.shortcuts import render
from reservation.models import *

def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "reservation/rooms_list.html", context)
