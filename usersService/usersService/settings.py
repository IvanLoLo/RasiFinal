"""
Django settings for rasi project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv
#from djongo import base

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_j*#83ja-qzon$bk#*bfgy2@palyr8($)$&1i2-0dy=o324tdo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'users',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',  # Replace with your Redis server address and database number
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

ROOT_URLCONF = 'usersService.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'usersService.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

"""

DB_USERNAME = config('DB_USERNAME', default='admin')
DB_PASSWORD = config('DB_PASSWORD', default='admin_password')
DB_HOST = config('DB_HOST', default='34.132.173.31')
DB_PORT = config('DB_PORT', default=27017, cast=int)
DB_NAME = config('DB_NAME', default='your_database_name')

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': DB_NAME,
        'ENFORCE_SCHEMA': False,  # Set this to False if you don't want to enforce schema
        'CLIENT': {
            'host': DB_HOST,  # Replace with your MongoDB host
            'port': DB_PORT,  # Replace with your MongoDB port
            'username': DB_USERNAME,  # Replace with your MongoDB username
            'password': DB_PASSWORD,  # Replace with your MongoDB password
            'authSource': 'admin',  # Replace with your MongoDB authentication source
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'https://rasi.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F{{ip_publica_instancia}}:8080'
SOCIAL_AUTH_TRAILING_SLASH = False
SOCIAL_AUTH_AUTH0_DOMAIN = 'rasi.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'hfP90WL51axfipuf8n1FmlypHLt6Or15'
SOCIAL_AUTH_AUTH0_SECRET = '7xRWgxvaMMf63gTQhFJ0cf2lP23e0uTo29YGC4A7vHrjp7HeipZO6FhlZzq8S4rp'

SOCIAL_AUTH_AUTH0_SCOPE = [
 'openid',
 'profile',
 'email',
 'role',
]

AUTHENTICATION_BACKENDS = {
 'usersService.auth0backend.Auth0',
 'django.contrib.auth.backends.ModelBackend',
}