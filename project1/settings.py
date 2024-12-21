"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%&twe6^nv#y6$gggm_09orki@-qu3_phf@t=jc0jdof9^i@$45'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', 
    'django.contrib.sessions', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'signup',
    'login',
    'search',
    'cart',
    'ColdAndFlu',
    'contact',
    'home',
    'notification',
    'PainRelief',
    'payment',
    'administrator',
    'products',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

# allauth settings
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", 
    'social_core.backends.facebook.FacebookOAuth2',
)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', 
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
        'redirect_uri': 'http://127.0.0.1:8000/accounts/google/login/callback/'  # Make sure this matches the Google API setting
    },
}

# settings.py



ROOT_URLCONF = 'project1.urls'

import os 

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
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]



WSGI_APPLICATION = 'project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medkink',
        'USER': 'medkink_user',
        'PASSWORD': 'yourpassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'TEST': {
            'NAME': 'test_medkink',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    },
}






# Configure the site ID (used by allauth for social login)
SITE_ID = 2




LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# LOGIN_REDIRECT_URL = '/home/'

# LOGOUT_REDIRECT_URL = "/"

LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
LOGOUT_REDIRECT_URL = '/login/'  # Redirect to login after logout

 

SOCIAL_AUTH_SECRET_KEY = "1301591854300852"
SOCIAL_AUTH_SECRET_SECRET = '8579c726612e0628099a20256aaef5fe'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


SOCIAL_AUTH_GOOGLE_CLIENT_ID = "501183785532-iaeloovus3e40n15j47ht8ek8no34bun.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_SECRET = "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"



ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ydark343@gmail.com'
EMAIL_HOST_PASSWORD = '@yousefdark1@'



PAYMOB_API_KEY = 'ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2TVRBeE16WTNNQ3dpYm1GdFpTSTZJbWx1YVhScFlXd2lmUS4tazNtVk9xaTVwVzI2Z0MyVHVLZWF2OHg3bTBpMHcyNXczc21qVVdQZjBDZUtsV3BNcTZOT3ExQU0tdU5yZ25kM1hQOFpES2VJcW1BTTJvd1pndUxSdw=='
PAYMOB_SECRET_KEY = 'egy_sk_test_3c4d75e9a9a6c248d4cde01d74a883b1367b987d1b85c636a0b1eaff6a9be2db'
# In settings.py
PAYMOB_INTEGRATION_ID = 'egy_pk_test_MVlyVyX07lftynLFQyZkRiMJXMqcbEEq'


# settings.py

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Uses database to store session data
SESSION_COOKIE_AGE = 86400  # Session cookies expire in 24 hours
