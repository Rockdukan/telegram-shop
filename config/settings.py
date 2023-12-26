import os

from pathlib import Path

from split_settings.tools import include


ALLOWED_HOSTS = ['127.0.0.1', 'xn--80aadc4a6bn.xn--p1ai', 'http://37.140.192.71']

DEBUG = True

# AUTH_USER_MODEL = 'profile.User'
BASE_DIR = Path(__file__).resolve().parent.parent

# Internationalization settings
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'ru'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# URL settings
ROOT_URLCONF = 'config.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4)xgm#p_7)&iuek_qjcm+&+l&^8stqanzfz)h)@#9xgukk-0@^'

# Site settings
SITE_ID = 1

# jQuery settings
USE_DJANGO_JQUERY = True

# WSGI settings
WSGI_APPLICATION = 'config.wsgi.application'

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'config.middlewares.CurrentAppMiddleware',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Templates settings
TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (os.path.join(os.path.dirname(BASE_DIR), 'templates'),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Other apps
    'smart_selects',

    # Project apps
    'apps.shop',
    'apps.telegram_bot',
]

include(
    # BASE SETTINGS FROM PROJECT
    'components/caches.py',
    # 'components/robots.py',
    'components/session.py',

    # API SETTINGS
    # 'components/djoser.py',
    # 'components/rest_framework.py',
    # 'components/oauth2_toolkit.py',
    # 'components/simple_jwt.py',
    # 'components/yasg.py',

    # AUTHENTIFICATION SETTINGS
    # 'components/auth/account.py',
    # 'components/auth/socialaccount.py',

    # CUSTOM ADMIN
    # 'components/custom_admin/jazzmin.py',
    # 'components/custom_admin/simple_ui.py',

    # CUSTOM MODELS
    # 'components/custom_models/django_model_utils.py',
    # 'components/custom_models/django_mptt.py',

    # DATABASE SETTINGS
    # 'components/database/mysql.py',
    # 'components/database/postgresql.py',
    # 'components/database/redis.py',
    'components/database/sqlite.py',

    # DESIGN
    # 'components/design/sorl_thumbnail.py',

    # DEVELOPMENT
    # 'components/development/compressor.py',
    # 'components/development/debug_toolbar.py',
    #'components/development/logging.py',
    # 'components/development/silk.py',

    # FIELDS
    # 'components/fields/django_sortedm2m.py'

    # FILE MANAGERS
    # 'components/file_managers/filebrowser.py',
    # 'components/file_managers/filer.py',

    # FORMS
    # 'components/forms/floppy_forms.py'
    # 'components/forms/smart_selects.py'

    # GALLERIES
    # 'components/galleries/photologue.py',
    # 'components/galleries/starcross_gallery.py',

    # INTERNATIONALIZATION SETTINGS
    # 'components/internationalization/modeltranslation.py',
    # 'components/internationalization/rosetta.py',

    # PAYMENT SETTINGS
    # 'components/payment/robokassa.py',
    # 'components/payment/sberbank.py',

    # SMTP SETTINGS
    'components/smtp.py',

    # WYSIWYG EDITORS SETTINGS
    # 'components/wysiwyg/ckeditor.py',
    # 'components/wysiwyg/tinymce.py',
)

MEDIA_URL = '/media/'
if DEBUG:
    MEDIA_ROOT = f'{BASE_DIR}/media/'
else:
    MEDIA_ROOT = '/home/igor/Projects/telegram-shop/project/media'


# Static files (CSS, JavaScript, Images) settings
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
if DEBUG:
    STATIC_DIR = BASE_DIR / 'static'
else:
    STATIC_ROOT = '/home/igor/Projects/telegram-shop/project/static'
