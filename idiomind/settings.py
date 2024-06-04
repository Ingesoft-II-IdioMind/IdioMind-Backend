"""
Django settings for idiomind project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import json
from os import getenv,path
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import dj_database_url
import dotenv
import pymysql
import stripe

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env.local'

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = getenv('DJANGO_SECRET_KEY',get_random_secret_key()) #secret key de django
API_KEY = getenv('GEMINI_API_KEY',get_random_secret_key()) #key de la api de gemini




DEBUG = getenv('DEBUG','False') == 'True'
STRIPE_API_KEY = getenv('stripe.api_key',get_random_secret_key())
PAYPAL_CLIENT_ID = getenv('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = getenv('PAYPAL_CLIENT_SECRET')
BASE_URL = getenv('BASE_URL')

ALLOWED_HOSTS=getenv('DJANGO_ALLOWED_HOSTS','127.0.0.1,idiomind.shop,localhost,idiomind-backend-production.up.railway.app,idiomind-frontend.vercel.app,idiomind-frontend-git-h09-jeramirezcas-projects.vercel.app').split(',')
ALLOWED_HOST_PRODUCTION = getenv('ALLOWED_HOST_PRODUCTION')
DOMAIN = getenv('DOMAIN')
SITE_NAME = 'idiomind'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'cloudinary',
    'Accounts',
    'Documents',
    'Mazos',
    'Flashcard',
    'idiomas',
    'Notes',
    'djoser',
    'social_django',
    'Gramatica',
    'Fonetica',
    'Post',
    'Suscriptions',
    'Transacciones'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'idiomind.urls'

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

WSGI_APPLICATION = 'idiomind.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DEVELOPMENT_MODE = getenv('DEVELOPMENT_MODE','False')=='True'

if DEVELOPMENT_MODE is True:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'IDIOMIND_DATABASE',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }


}
else:
    DATABASES = {
        'default': dj_database_url.parse(getenv('DATABASE_URL'))
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATIC_ROOT = path.join(BASE_DIR, 'static')






AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'Accounts.authentication.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ]
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
RESEND_SMTP_PORT = 587
RESEND_SMTP_USERNAME = 'resend'
RESEND_SMTP_HOST = 'smtp.resend.com'
DEFAULT_FROM_EMAIL ="IdioMind@resend.dev"
RESEND_API_KEY = getenv('RESEND_API_KEY')
RESEND_SENDER = getenv('RESEND_SENDER')
RESEND_SUBJECT = getenv('RESEND_SUBJECT')


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL':'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':False,
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': getenv('REDIRECT_URLS','https://www.idiomind.shop/auth/google,http://127.0.0.1:3000/auth/google,https://idiomind-frontend-git-h09-jeramirezcas-projects.vercel.app/auth/google,https://idiomind-frontend.vercel.app/auth/google').split(',')
}

AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 60 * 2
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 *24
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv('GOOGLE_AUTH_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('GOOGLE_AUTH_SECRET_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

CORS_ALLOWED_ORIGINS = getenv('CORS_ALLOWED_ORIGINS','https://www.idiomind.shop,http://localhost:3000,http://127.0.0.1:3000,https://idiomind-frontend-git-h09-jeramirezcas-projects.vercel.app,https://idiomind-frontend.vercel.app,https://idiomind-backend-production.up.railway.app').split(',')
CORS_ALLOW_CREDENTIALS = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Accounts.UserAccount'


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': getenv('CLOUDINARY_API_SECRET'),
}
 
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
