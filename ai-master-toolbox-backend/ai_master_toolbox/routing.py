# routing.py

from django.urls import path, re_path
from chatgpt.views.chat_websocket import ChatWebSocket

websocket_urlpatterns = [
    path('ws/chat_socket/', ChatWebSocket.as_asgi()),
]
