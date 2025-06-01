from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

TARGET_ENV = os.getenv('TARGET_ENV', 'dev') # Default to 'dev' if TARGET_ENV is not set in .env

# Ensures NOT_PROD is True if TARGET_ENV is 'dev', 'local', or not explicitly 'prod*'
NOT_PROD = not TARGET_ENV.lower().startswith('prod')

if NOT_PROD:
    print("INFO: Running in NON-PRODUCTION (DEBUG) mode via settings.py")
    DEBUG = True
    SECRET_KEY = 'django-insecure-zot9349(=0kis++cts3*pv)osg1(8qz7*uy9)9y5w30yvt8+_w' # Standard insecure key for dev
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    print("INFO: Running in PRODUCTION mode via settings.py")
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1'] # DEBUG can still be True in "prod" if env var says so
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ') # Add default if env var is missing
    CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(' ') # Add default if env var is missing

    SECURE_SSL_REDIRECT = \
        os.getenv('SECURE_SSL_REDIRECT', '0').lower() in ['true', 't', '1']

    if SECURE_SSL_REDIRECT:
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    DATABASES = { # This is the production database block
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DBNAME'),
            'HOST': os.environ.get('DBHOST'),
            'USER': os.environ.get('DBUSER'),
            'PASSWORD': os.environ.get('DBPASS'),
            'OPTIONS': {'sslmode': 'require'}, # Ensure this is correct for your Postgres setup
        }
    }
    
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', # Django's runserver will NOT serve static files. WhiteNoise will.
    'loja', # Sua aplicação 'loja'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise middleware - importante que venha cedo
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MARKETOON.urls' # Certifique-se que 'MARKETOON' é o nome correto do seu diretório de projeto

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Se você tiver uma pasta 'templates' na raiz do projeto (nível de manage.py), adicione-a aqui:
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [], # Deixe vazio se seus templates estão apenas dentro das apps
        'APP_DIRS': True, # Permite que o Django encontre templates em 'loja/templates/', etc.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MARKETOON.wsgi.application' # Certifique-se que 'MARKETOON' é o nome correto

# A configuração de DATABASES agora é feita exclusivamente no bloco if NOT_PROD / else no topo.

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'pt-br' # Ajustado para Português do Brasil
TIME_ZONE = 'America/Recife' # Ajustado para fuso horário de Recife
USE_I18N = True
USE_TZ = True # USE_L10N é obsoleto; USE_TZ controla a consciência de fuso horário

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/') # URL para referenciar arquivos estáticos (normalmente '/static/')

# Diretório onde o `collectstatic` irá copiar todos os arquivos estáticos para produção.
# WhiteNoise servirá desta pasta em produção.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected') # Você pode nomear como 'staticfiles' se preferir

# Lista de diretórios onde o Django (e WhiteNoise) procurarão por arquivos estáticos adicionais,
# além das pastas 'static' dentro de cada app (como 'loja/static/').
# Sua imagem 'logo.png' está em 'loja/static/img/logo.png' e será encontrada por estar em uma app.
# A linha abaixo é para uma pasta 'static' global na raiz do projeto.
# Se você não tiver essa pasta global, esta linha pode ser uma lista vazia `[]` ou removida.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Backend de armazenamento para WhiteNoise, otimizado para produção.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout URLs
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Media files (arquivos enviados por usuários)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'