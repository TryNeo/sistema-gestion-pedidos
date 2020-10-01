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
        'NAME': 'd49vlqkfkje3d3',
        'USER': 'eydoiyghwobtgm',
        'PASSWORD': '1765ad9872f7bcd236abb56231fbe7b7f93900344373b734bcb3c90dee6a36b6',
        'HOST': 'ec2-52-207-124-89.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


STATICFILES_DIRS = (BASE_DIR, "static")
