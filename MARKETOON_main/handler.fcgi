import sys
import os

# Defina o caminho para seu projeto
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MARKETOON.settings')

from django.core.wsgi import get_wsgi_application
from wfastcgi import run

wsgi_app = get_wsgi_application()
run(wsgi_app)
