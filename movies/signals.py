import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cinema, Room, Movie, Screening
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Cinema)
@receiver(post_save, sender=Room)
@receiver(post_save, sender=Movie)
@receiver(post_save, sender=Screening)
def notify_refresh(sender, instance, **kwargs):
    channel_layer = get_channel_layer()

    # Use async_to_sync to call async function inside a sync function
    async_to_sync(channel_layer.group_send)(
        "refresh_group",
        {"type": "refresh_message", "message": "refresh"}  # Match the expected message in JS
    )