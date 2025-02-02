from django.shortcuts import render, get_object_or_404
from .models import Cinema, Room, Screening

def index(request):
    cinemas = Cinema.objects.all()
    return render(request, 'movies/index.html', {'cinemas': cinemas})

def cinema_detail(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    screenings = Screening.objects.filter(room__cinema=cinema).order_by('screening_time').filter(display=True)
    return render(request, 'movies/details.html', {'cinema': cinema, 'screenings': screenings})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    screenings = room.screening_set.filter(display=True).order_by('screening_time')
    screening = screenings.first() if screenings.exists() else None
    return render(request, 'movies/room_details.html', {'room': room, 'screening': screening, 'screenings': screenings})
