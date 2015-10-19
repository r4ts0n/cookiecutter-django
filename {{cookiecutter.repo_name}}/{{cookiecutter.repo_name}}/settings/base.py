"""
Django settings for {{ cookiecutter.repo_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import environ

from django.utils.translation import ugettext_lazy as _


BASE_DIR = environ.Path(__file__) - 4

env = environ.Env()

DEBUG = env.bool('DJANGO_DEBUG', False)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    {% if cookiecutter.use_django_cms == 'y' -%}
    'django.contrib.sites',
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_admin_style',
    {%- endif %}
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    {% if cookiecutter.use_django_cms == 'y' -%}
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    {%- endif %}
)

{% if cookiecutter.use_django_cms == 'y' -%}
SITE_ID = 1

LANGUAGES = (
    ('en-us', _('English')),
)
{%- endif %}

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                {% if cookiecutter.use_django_cms == 'y' -%}
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                {%- endif %}
            ],
        },
    },
]

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default='postgres://localhost/{{ cookiecutter.repo_name }}'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
