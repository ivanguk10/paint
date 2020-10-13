"""
WSGI config for paint project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/paint')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paint.settings')

application = get_wsgi_application()
