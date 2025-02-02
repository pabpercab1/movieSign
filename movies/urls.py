from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cinema_id>/", views.cinema_detail, name="details"),
    path("room/<int:room_id>/", views.room_detail, name="room_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)