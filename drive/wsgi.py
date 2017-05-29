"""
WSGI config for drive project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

sys.path.append(os.path.join(BASE_DIR, 'drive'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drive.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
