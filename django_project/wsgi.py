"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

os.environ['SECRET_KEY'] = 'QKRf5WEpV5H5HzLPzF8kwqCzWl0aFkkfSU6IBvrt1T0'
# os.environ['DEBUG'] = 'False'
os.environ['DATABASE_URL'] = 'mysql://Kimzaf:cHEZ%40na%4086@Kimzaf.mysql.pythonanywhere-services.com/Kimzaf$bloapidb'

path = '/home/Kimzaf/kimzaf.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()