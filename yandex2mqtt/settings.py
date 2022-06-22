"""
Django settings for yandex2mqtt project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

VENDOR_APPS = [
    'oauth2_provider',
    'corsheaders'
]

# apps.*
PROJECT_APPS = [
    'apps.mqtt',
    'apps.yandex',
    'apps.main',
]

INSTALLED_APPS = DJANGO_APPS + VENDOR_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yandex2mqtt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 'templates'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'yandex2mqtt.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DEFAULT_DB = 'default'

DATABASES = {
    DEFAULT_DB: env.db('DATABASE_URL', default='postgres:///yandex2mqtt'),
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
DEFAULT_TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

DEBUG_FILE = os.path.join(LOGS_DIR, 'debug.log')
ERROR_FILE = os.path.join(LOGS_DIR, 'error.log')

MB_10 = 10 * 1024 * 1024

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-8s %(name)-7s %(asctime)-25s %(module) %(process:d) %(thread:d) %(message)s',
        },
        'simple': {
            'format': '%(levelname)-8s %(name)-7s %(asctime)-25s %(message)s',
        },
        'color_simple': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(levelname)-8s %(name)-7s %(asctime)-25s %(message)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
        }
    },
    'handlers': {
        'file-debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,  # keep at most 10 log files
            'maxBytes': MB_10,
            'filename': DEBUG_FILE,
            'formatter': 'simple',
        },
        'file-error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,  # keep at most 10 log files
            'maxBytes': MB_10,
            'filename': ERROR_FILE,
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'color_simple',
        },
    },
    'loggers': {
        'mqtt': {
            'handlers': ['file-debug', 'file-error', 'console'],
            'level': 'DEBUG'
        },
        'yandex': {
            'handlers': ['file-debug', 'file-error', 'console'],
            'level': 'DEBUG'
        }
    }
}

WEBPACK_DEV_SERVER = DEBUG

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '/',  # must end with slash
        'STATS_FILE': str(os.path.join(BASE_DIR, 'frontend/webpack-stats.json')),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map'],
    }
}

LOGIN_URL = '/admin/login/'
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]
OAUTH2_PROVIDER = {
    "PKCE_REQUIRED": False
}
APPEND_SLASH = False

AUTHENTICATION_BACKENDS = [
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
]
AUTH_USER_MODEL = 'main.User'
