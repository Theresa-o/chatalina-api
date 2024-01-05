import os
import sys
from pathlib import Path

import api.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from api.middleware import TokenAuthMiddleware
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
        "websocket": TokenAuthMiddleware(URLRouter(api.routing.websocket_urlpatterns)),
    }
)

# ==============
# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatalina.settings")
# django_asgi_app = get_asgi_application()

# import api.routing

# application = ProtocolTypeRouter(
#     {
#         "http": django_asgi_app,
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(api.routing.websocket_urlpatterns))
#         ),
#     }
# )