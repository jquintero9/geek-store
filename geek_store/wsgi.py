"""
WSGI config for geek_store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
'''
whitenoise es una libreria que permite a las aplicaciones
web de python gestionar el almacenamiento de los archivos
estaticos.
'''
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geek_store.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)