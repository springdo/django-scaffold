"""
ASGI config for site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django_site.preps import set_default_env, load_sample_data

set_default_env()
load_sample_data()

application = get_asgi_application()
