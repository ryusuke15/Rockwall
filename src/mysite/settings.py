import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!(60c504rrcvy*pdt9vzw-5%8#rmssnv7_#f6%jo!*g7lj6yjz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["52.202.53.10","localhost", "rockwallstudios.nyc","www.rockwallstudios.nyc"]

#Email Setup
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rockwall.mgmt@gmail.com'
EMAIL_HOST_PASSWORD = 'ptwftqvgubwzxxym'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third Party App     
    'easy_thumbnails',
    'djangobower',
    'djangoseo',
    'django_markup',
    'image_cropping',
    'materializecssform',
    'pagedown',
    'robots',
    'sass_processor',
    'storages',
    #MyApp     
    'studio',
    'event_space',
    'coffee_shop',
    'django.contrib.sitemaps',
]

#Bower
BOWER_INSTALLED_APPS = (
    'angular',
    'foundation',
    'jquery',
    'materialize',
    'readmore-js',
)

#Easy_Thumbnail
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

#Django-Image-Cropping
IMAGE_CROPPING_THUMB_SIZE = (500, 500)


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

#Djnago Site
SITE_ID = 1

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rockwall',
        'USER': 'rockwalluser',
        'PASSWORD': 'silverchicken771',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media Files 
access_key = 'AKIAJHTCDKXITBQSSUKQ'
secret_key = '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'
AWS_ACCESS_KEY_ID = access_key
AWS_SECRET_ACCESS_KEY = secret_key
AWS_STORAGE_BUCKET_NAME = 'rockwall'
S3_URL = '//%s.s3.amazonaws.com/' %AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL + "media/"
DEFAULT_FILE_STORAGE = 'mysite.s3utils.MediaRootS3BotoStorage'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
AWS_PRELOAD_METADATA = True 
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

#STATIC Files
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
        ]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static") 

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'sass_processor.finders.CssFinder',
]

#ADMIN 
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
GRAPPELLI_ADMIN_TITLE = 'Rockwall Studios'
