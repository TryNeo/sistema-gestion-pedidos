from SistemaGestionPedidos.settings.base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['asoprotosue-pedidos.herokuapp.com']


"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dd871io8kp5hst',
        'USER': 'tacjuwgwwbvpqq',
        'PASSWORD': 'a59525678934edac268d0c9c808c5276fefcde29a8c0e9c65a75b58ddac34b73',
        'HOST': 'ec2-52-72-34-184.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


STATICFILES_DIRS = (BASE_DIR, "static")
