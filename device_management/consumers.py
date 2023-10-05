import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Devices
from .serializers import DevicesSerializer


class DeviceStatusConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.room_name = None

    async def connect(self):
        self.room_name = "device"
        self.room_group_name = "device_group"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        data = await self.get_device_objects()
        await self.send(text_data=json.dumps({"msg": "connected", "data": data}))

    @database_sync_to_async
    def get_device_objects(self):
        # Fetch device objects synchronously
        devices = Devices.objects.all()
        serializer = DevicesSerializer(devices, many=True)
        return serializer.data

    async def disconnect(self, close_code):
        pass

    async def notify_device_update(self, event):
        await self.send(text_data=json.dumps(event["event"]))
