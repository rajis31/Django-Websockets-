from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path("ws/test", consumer.MainConsumer.as_asgi()),
]
