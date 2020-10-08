"""
Django settings for ebdjango project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0bgnw^0tw64h+0v+-vk1kvroc-=43a62w+u*629+sb%3&#)av0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'guork-env.trawp8wvmc.us-east-1.elasticbeanstalk.com',
    'guork.mx',
    'www2.guork.mx',
    'www.guork.mx',
    'guork.herokuapp.com'
]

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'ventas.venezum@gmail.com'
# EMAIL_HOST_PASSWORD = 'Cas8735839*'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Venezum'
#
# MANAGERS = [
#     ("Carlos Blanco", "venezum2018@gmail.com")
# ]
#
# ADMINS = [
#     ("Carlos Blanco", "venezum2018@gmail.com")
# ]

LOGIN_URL = '/login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'stripe',
    'storages',

    # my apps
    'accounts',
    'billing',
    'blog',
    'courses',
    'stripe_checkout',

]

AUTH_USER_MODEL = 'accounts.User'  # changes the built-in user model to ours
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/login/'

FORCE_SESSION_TO_ONE = False
FORCE_INACTIVE_USER_ENDSESSION = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ebdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ebdjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = '/static/'

LOCAL_STATIC_CDN_PATH = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')

STATIC_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'static')  # live cdn AWS S3

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'media')
MEDIA_URL = '/media/'  # django-storages

from ebdjango.aws.conf import *

# CKEDITOR
CKEDITOR_UPLOAD_PATH = "ckuploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
    },
}

DATE_INPUT_FORMATS = ['%d/%m/%Y']

# GOOGLE RECAPTCHA

GOOGLE_RECAPTCHA_PUBLIC_KEY = '6LdbV78UAAAAAIpRxHyNTJrb6W0YZd61RKEPFdh1'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LdbV78UAAAAAE_vo9kwHndz9IJiaxyerDeWxrzf'

# STRIPE

STRIPE_PUB_KEY = 'pk_test_UTSbSt5W4QpVCHpCxa5K7nIw00FbA6R0K2'
STRIPE_SECRET_KEY = 'sk_test_KJ6abjyErxo9HcttWkkdIEGW00QGzanzow'

CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
