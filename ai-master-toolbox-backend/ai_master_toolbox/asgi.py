"""
ASGI config for ai_master_toolbox project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_master_toolbox.settings')
django.setup()  # 初始化Django设置
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(routing.websocket_urlpatterns),
})
