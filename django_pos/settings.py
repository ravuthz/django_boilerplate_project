"""
Django settings for django_pos project.

Generated by 'django-admin startproject' using Django 3.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

import dj_database_url
import environ

env = environ.Env(
    ENV=(str, 'production'),
    DEBUG=(bool, False),
    ADMIN_URL=(str, 'adminz/'),
    TIME_ZONE=(str, 'Asia/Phnom_Penh'),
    SECRET_KEY=(str, 'S3cRétK3yH3rë'),
    LANGUAGE_CODE=(str, 'en-us'),
    ALLOWED_HOSTS=(str, '*'),
    DJANGO_STATIC_HOST=(str, ''),
    INTERNAL_IPS=(str, ''),
)

env.read_env(env.str('ENV_PATH', '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h%g0b1oq&y&x6=dhttpb8wk%8=sixw6ct)6&s&3e(kl88r5dn_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Commom packages
    'phonenumber_field',
    'django_extensions',
    'debug_toolbar',
    'model_utils',
    'django_seed',
    'django_admin_shell',
    'explorer',
    'django_sql_dashboard',
    'simple_history',
    'modeltranslation',
    # Core application
    'core',
    'apps.settings',
    'apps.products',
    'apps.users',
    'apps.carts',
    'apps.orders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'django_pos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'django_pos.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if env('DATABASE_URL') is not None:
    DATABASES['default'] = dj_database_url.config(env="DATABASE_URL", conn_max_age=600, ssl_require=False)

if env('DATABASE_DASHBOARD_URL') is not None:
    DATABASES['dashboard'] = dj_database_url.config(env="DATABASE_DASHBOARD_URL", conn_max_age=600, ssl_require=False)

INTERNAL_IPS = env('INTERNAL_IPS').split(" ")

EXPLORER_CONNECTIONS = {'Default': 'default'}
EXPLORER_DEFAULT_CONNECTION = 'default'

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('kh', gettext('Khmer')),
)
MODELTRANSLATION_LANGUAGES = ('en', 'kh')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'kh')
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

# STATIC_HOST = env("STATIC_HOST", default="")

# STATIC_URL = STATIC_HOST + "/static/"
# STATIC_ROOT = env("STATIC_ROOT", default=os.path.join(BASE_DIR, "static/files"))
#
# MEDIA_URL = STATIC_HOST + "/media/"
# MEDIA_ROOT = env("MEDIA_ROOT", default=os.path.join(BASE_DIR, "static/medias"))
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     # "/var/www/static/"
# ]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
