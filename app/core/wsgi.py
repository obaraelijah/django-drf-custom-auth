import os
from decouple import config
from django.core.wsgi import get_wsgi_application

environment = config('ENVIRONMENT')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings."+environment)

application = get_wsgi_application()
