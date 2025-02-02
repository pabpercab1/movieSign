from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="cinema_logos/", blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    movies = models.ManyToManyField("Movie", through="Screening")

    def __str__(self):
        return str(self.cinema) + ": " + str(self.name)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    poster = models.ImageField(upload_to="movie_posters/", blank=False, null=False, default="movie_posters/default.jpg")

    def __str__(self):
        return str(self.title) + ": " + str(self.description)

class Screening(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('doorsopen', 'Doors Open'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screening_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    display = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.screening_time} || {self.movie} || {self.room}"