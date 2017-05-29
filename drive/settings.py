# Env vars to set:
# SLACK_CLIENT_SECRET
# SLACK_CLIENT_ID
#

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

ALLOWED_HOSTS = ['*']

DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = os.environ.get('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django_slack_oauth',
  'bootstrap3',
  'motions.apps.MotionsConfig',
  'vote',
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

ROOT_URLCONF = 'drive.urls'

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

WSGI_APPLICATION = 'drive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
  }
}
# Update database configuration with $DATABASE_URL.
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Slack credentials
SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.environ.get('SLACK_CLIENT_SECRET')
SLACK_SCOPE = 'admin,bot'
SLACK_SUCCESS_REDIRECT_URL = '/motions'

SLACK_PIPELINES = [
    'drive.pipelines.debug_oauth_request',
    'drive.pipelines.register_user',
    'drive.pipelines.log_user_in',
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Get local settings from local_settings
try:
    from .local_settings import *
except ImportError:
    pass
