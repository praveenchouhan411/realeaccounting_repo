"""
Django settings for realeaccounting project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.mail import send_mail

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_FOLDER = os.getcwd()

EMAL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'praveensinghc0@gmail.com'
EMAIL_HOST_PASSWORD = 'Pr@veen1004'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""

#EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'praveensinghc0@gmail.com'
EMAIL_HOST_PASSWORD = 'Pr@veen1004'
EMAIL_USE_TLS = True
ACCOUNT_EMAIL_VERIFICATION = "none"
REGISTRATION_EMAIL_HTML = False


"""
EMAIL_HOST = 'my-domain.com'
EMAIL_HOST_PASSWORD = 'my cpanel password'
EMAIL_HOST_USER = 'my cpanel user'
EMAIL_PORT      = 25
EMAIL_USE_TLS   = False
DEFAULT_FROM_EMAIL  = 'webmaster@my-host.com'
SERVER_EMAIL    = 'root@my-domain.com'
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@!s=ek*p-n--u^u74kjfxm-2csffi0sim0*80#eazasyl%25go'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'realeaccounting.urls'

ACCOUNT_ACTIVATION_DAYS = 7

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'main-templates'), os.path.join(PROJECT_DIR, 'main-templates/registration')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ]
        },	
	    
    },
]

WSGI_APPLICATION = 'realeaccounting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {

    'default': 
     {

        'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.db.sqlite3',
        #'NAME': os.path.join(PROJECT_FOLDER, 'db.sqlite3'), 
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '',
    }

}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_FOLDER, 'db.sqlite3'),  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
"""
      
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    #PUT STRING HERE
    #home/praveen/Documents/python/my-project/django_project
    ('assets', '/home/praveen/Documents/python/my-project/realeaccounting/realeaccounting/assets'),
)

