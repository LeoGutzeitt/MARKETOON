import sys
import os

# Define o diretório base e configura o path
sys.path.append(os.path.dirname(__file__))

# Configurações Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MARKETOON.settings')

# Importa o handler WSGI da aplicação
from django.core.wsgi import get_wsgi_application
from wfastcgi import WSGIHandler

# Define o handler para o IIS
wsgi_app = get_wsgi_application()
handler = WSGIHandler(wsgi_app)
