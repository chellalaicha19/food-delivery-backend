"""
WSGI config for food_del_back project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'food_del_back.deployement_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'food_del_back.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_del_back.settings')

application = get_wsgi_application()
