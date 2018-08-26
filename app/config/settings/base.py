"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import json
import os
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


SECRETS_MODULES = {
    # Module's full path string
    'raven': 'raven',
    # Python module object
    'requests': requests,
}

# SECRETS
# if 'TRAVIS_PULL_REQUEST' in os.environ:
#     print(os.environ)
#     if os.environ['TRAVIS_PULL_REQUEST'] is False:
#         print('pr 요청이 아닌 경우')
#         print(os.environ['TRAVIS_PULL_REQUEST'])
#         SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
#         SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
#         SECRETS = json.loads(open(SECRETS_BASE, 'rt').read())
#         SECRET_KEY = SECRETS['SECRET_KEY']
#
#         # AWS
#         AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
#         AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
#         AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
#         AWS_S3_REGION_NAME = SECRETS['AWS_S3_REGION_NAME']
#         AWS_S3_SIGNATURE_VERSION = SECRETS['AWS_S3_SIGNATURE_VERSION']
#         AWS_DEFAULT_ACL = SECRETS['AWS_DEFAULT_ACL']
#         AWS_ELASTIC_CACHE = SECRETS['AWS_ELASTIC_CACHE']
#
#         # CREATE SUPER USER
#         SUPERUSER_USERNAME = SECRETS['SUPERUSER_USERNAME']
#         SUPERUSER_PASSWORD = SECRETS['SUPERUSER_PASSWORD']
#         SUPERUSER_EMAIL = SECRETS['SUPERUSER_EMAIL']
print('base.py')
print(os.environ)
if os.environ.get('TRAVIS'):
    print(os.environ.get('TRAVIS_PULL_REQUEST'))
    if os.environ.get('TRAVIS_PULL_REQUEST') is False:
        print(os.environ)
        SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
        SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
        SECRETS = json.loads(open(SECRETS_BASE, 'rt').read())
        SECRET_KEY = SECRETS['SECRET_KEY']
        # AWS
        AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
        AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
        AWS_S3_REGION_NAME = SECRETS['AWS_S3_REGION_NAME']
        AWS_S3_SIGNATURE_VERSION = SECRETS['AWS_S3_SIGNATURE_VERSION']
        AWS_DEFAULT_ACL = SECRETS['AWS_DEFAULT_ACL']
        AWS_ELASTIC_CACHE = SECRETS['AWS_ELASTIC_CACHE']

        # CREATE SUPER USER
        SUPERUSER_USERNAME = SECRETS['SUPERUSER_USERNAME']
        SUPERUSER_PASSWORD = SECRETS['SUPERUSER_PASSWORD']
        SUPERUSER_EMAIL = SECRETS['SUPERUSER_EMAIL']
else:
    SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
    SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
    SECRETS = json.loads(open(SECRETS_BASE, 'rt').read())
    SECRET_KEY = SECRETS['SECRET_KEY']
    # AWS
    AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = SECRETS['AWS_S3_REGION_NAME']
    AWS_S3_SIGNATURE_VERSION = SECRETS['AWS_S3_SIGNATURE_VERSION']
    AWS_DEFAULT_ACL = SECRETS['AWS_DEFAULT_ACL']
    AWS_ELASTIC_CACHE = SECRETS['AWS_ELASTIC_CACHE']

    # CREATE SUPER USER
    SUPERUSER_USERNAME = SECRETS['SUPERUSER_USERNAME']
    SUPERUSER_PASSWORD = SECRETS['SUPERUSER_PASSWORD']
    SUPERUSER_EMAIL = SECRETS['SUPERUSER_EMAIL']

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'members.User'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',

    'books',
    'members',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
        ],
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

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
