"""
Django settings for CarolsClass project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import logging
import django.utils.log
import logging.handlers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eo2da!s0ne3^g7-tbw(3)om3rc9!@tt3d_0j_8x#jdn#nh!u5!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'django.contrib.sitemaps',
    'blog',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.weibo',
    'djcelery',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CarolsClass.urls'

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

WSGI_APPLICATION = 'CarolsClass.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carolsclass',  # 数据库名
        'USER': 'root',  # 用户名
        'PASSWORD': 'hujie2007',  # 密码
        'HOST': 'localhost',  # 数据库主机，默认为localhost
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR,'avatar'), )


MEDIA_URL = '/meida/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'meida').replace('\\', '/')


CKEDITOR_JQUERY_URL = '//cdn.bootcss.com/jquery/1.11.3/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads"

APP_ID = 'wxb950784440d6b5ab'
APP_SECRET = '904063a29559a3e14f7f7e121c179f64'

import djcelery

djcelery.setup_loader()

BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_IMPORTS = ('wechat.task')

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

LOGIN_REDIRECT_URL = '/'
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'mboneauto@163.com'
EMAIL_HOST_PASSWORD = 'hujie2007'
EMAIL_PORT = 25

ACCOUNT_EMAIL_VERIFICATION =  'none'

DEFAULT_FROM_EMAIL = 'Auto <mboneauto@163.com>'

AUTH_USER_MODEL = 'blog.User'