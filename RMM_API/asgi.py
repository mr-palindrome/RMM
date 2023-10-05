"""
ASGI config for RMM_API project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include

from device_management import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RMM_API.settings")

application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(routing.websocket_urlpatterns),
        "http": get_asgi_application(),
    }
)
