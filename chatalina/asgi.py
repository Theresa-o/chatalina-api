"""
ASGI config
 
It exposes the ASGI callable as a module-level variable named ``application``.
 
For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
 
"""
import os
import sys
from pathlib import Path

from chatalina import routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
 
# This allows easy placement of apps within the interior
 
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "chatalina"))
 
# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'chatalina.settings')
 
# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()
  
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(routing.websocket_urlpatterns),
    }
)