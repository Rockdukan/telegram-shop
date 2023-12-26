"""Modeltranslation settings"""


LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

MODELTRANSLATION_CUSTOM_FIELDS = ()

MODELTRANSLATION_DEBUG = False

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_ENABLE_FALLBACKS = True

MODELTRANSLATION_LANGUAGES = ('en', 'ru')

MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'ru')

MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

MODELTRANSLATION_LOADDATA_RETAIN_LOCALE = True

# Modeltranslation использует функцию авторегистрации, аналогичную функции
# администратора Django. Процесс авторегистрации будет искать translation.py
# в корневом каталоге каждого приложения, находящегося в INSTALLED_APPS.
# Данная настройка предназначена для расширения учитываемых модулей.
MODELTRANSLATION_TRANSLATION_FILES = ()
