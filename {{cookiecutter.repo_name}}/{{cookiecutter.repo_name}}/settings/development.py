from .base import *  # noqa


DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!!')

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
