"""
ASGI config for oma_k_ron project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if os.path.isfile('env.py'):
    import env

development = os.environ.get("DEVELOPMENT", False)


if development == 'True':
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'oma_k_ron.dev_settings',
    )
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'oma_k_ron.prod_settings',
    )

application = get_asgi_application()
