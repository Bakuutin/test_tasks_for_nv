import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = '!dmnqzs5e=utxa9j8b9c0=xs3!&y%$#yd-x543b&sq#uq1t^v*'

DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_URL = 'http://127.0.0.1:8000/'

INSTALLED_APPS = [
    'nv',
]

ROOT_URLCONF = 'nv.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nv',
    }
}

WSGI_APPLICATION = 'nv.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

APPEND_SLASH = True
