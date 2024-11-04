from django.urls import re_path

from websocket import consumers

websocket_urlpatterns = [
    re_path(r"ws/animation/888888", consumers.AnimationConsumer.as_asgi()),
]