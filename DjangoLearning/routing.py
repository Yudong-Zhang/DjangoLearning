from django.urls import re_path
from websocket import consumers

websocket_urlpatterns = [
    re_path("ws/animation/888888/", consumers.AnimationConsumer.as_asgi()),
    # re_path("ws/animation/666666/", consumers_2.AnimationConsumer2.as_asgi())
]