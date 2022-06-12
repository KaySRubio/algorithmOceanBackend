"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# Configure Django App for Heroku
import django_heroku

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-ihphlco8y6n^q1h3#9j-lsmb^fphx@----dco@o2kcc$t+w@6&'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['https://algorithmoceanbackend.herokuapp.com/', 'algorithmoceanbackend.herokuapp.com', 'localhost:8000', 'http://localhost:8000/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'algorithmOcean',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000',
     'https://localhost:3000',
     'http://10.0.0.202:3000',
     'https://stormy-sierra-07970.herokuapp.com',
     'https://algorithmoceanbackend.herokuapp.com/',
     #'algorithmoceanbackend.herokuapp.com'
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000', 
    'http://localhost', 
    'https://localhost:3000', 
    'http://10.0.0.202:3000', 
    'https://stormy-sierra-07970.herokuapp.com',
    'https://algorithmoceanbackend.herokuapp.com/',
    #'algorithmoceanbackend.herokuapp.com'
]

AUTH_USER_MODEL = 'algorithmOcean.CustomUser' #new

CSRF_COOKIE_NAME = "csrftoken"
#CSRF_COOKIE_NAME = "CSRF_COOKIE"

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Authorization',
    'Content-Type',
    'X-CSRFToken',
    'Access-Control-Allow-Origin'
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000', 
    'http://localhost', 
    'https://localhost:3000', 
    'http://10.0.0.202:3000', 
    'https://stormy-sierra-07970.herokuapp.com',
    'https://stormy-sierra-07970.herokuapp.com/createaccount',
    'https://stormy-sierra-07970.herokuapp.com/login',
    'https://algorithmoceanbackend.herokuapp.com'#,
    #'algorithmoceanbackend.herokuapp.com'
]

CORS_ALLOW_CREDENTIALS = True

#CSRF_HEADER_NAME = 'X-CSRFToken'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'

#CSRF_COOKIE_DOMAIN = [
#    'algorithmoceanbackend.herokuapp.com',
#    'stormy-sierra-07970.herokuapp.com',
#]
#    'http://localhost:3000', 
#    'http://localhost:8000', 
#    '10.0.0.202:3000', 
#    '10.0.0.202', 
#    'localhost:3000', 
#    'localhost', 
#    'https://localhost:3000', 
#    'http://10.0.0.202:3000', 
#    'https://stormy-sierra-07970.herokuapp.com', 
#    'https://localhost:3000/login',
#    'https://algorithmoceanbackend.herokuapp.com/',
#    'algorithmoceanbackend.herokuapp.com',
#    '.herokuapp.com'
#]

CSRF_COOKIE_HTTPONLY = False
#CSRF_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
#LOGIN_REDIRECT_URL = "/"

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configure Django App for Heroku
django_heroku.settings(locals())