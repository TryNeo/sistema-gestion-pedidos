from SistemaGestionPedidos.settings.base import *
import dj_database_url
from decouple import config
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['asoprotosue-pedidos.herokuapp.com']


"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
#Prueba
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


STATICFILES_DIRS = (BASE_DIR, "static")