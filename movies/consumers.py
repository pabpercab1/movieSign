import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class RefreshConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connected!")
        await self.channel_layer.group_add("refresh_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected: {close_code}")
        await self.channel_layer.group_discard("refresh_group", self.channel_name)

    async def refresh_message(self, event):
        logger.info(f"Received Redis message: {event}")
        await self.send(text_data=json.dumps({"message": event["message"]}))