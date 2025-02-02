from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/refresh/$', consumers.RefreshConsumer.as_asgi()),
]