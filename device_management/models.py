from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Devices(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.name


@receiver(post_save, sender=Devices)
def device_updated(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    event = {
        "id": instance.id,
        "name": instance.name,
        "status": instance.status,
        "updated_at": str(instance.updated_at),
    }
    async_to_sync(channel_layer.group_send)(
        "device_group", {"type": "notify_device_update", "event": event}
    )
