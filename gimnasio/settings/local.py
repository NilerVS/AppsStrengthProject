from .base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret ('BD_NAME'),
        'USER': get_secret ('USER'),
        'PASSWORD': get_secret ('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

STATICFILES_DIRS  = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


