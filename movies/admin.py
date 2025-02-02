from django.contrib import admin
from .models import Cinema, Room, Movie, Screening

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(Screening)