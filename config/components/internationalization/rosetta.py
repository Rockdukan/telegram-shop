"""Rosetta settings"""
from project.components.account import LOGIN_URL
from project.settings import LANGUAGES


GOOGLE_APPLICATION_CREDENTIALS_PATH = None

ROSETTA_AUTO_COMPILE = True

GOOGLE_PROJECT_ID = None

# Альтернативная функция (строка или вызываемая), которая определяет,
# может ли данный пользователь получить доступ к представлениям перевода.
# Эта функция получает пользователя в качестве аргумента и возвращает
# логическое значение, указывающее, разрешено ли переданному пользователю
# использовать Rosetta или нет.
# ROSETTA_ACCESS_CONTROL_FUNCTION

ROSETTA_CACHE_NAME = 'rosetta'

ROSETTA_ENABLE_REFLANG = False

# Включить предложения по переводу AJAX
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = False

ROSETTA_EXCLUDED_APPLICATIONS = ()

ROSETTA_EXCLUDED_PATHS = ()

ROSETTA_LANGUAGES = LANGUAGES

# Установите значение True, чтобы включить языковые группы, которые могут
# использоваться для предоставления разным переводчикам доступа к разным
# языкам. Вместо создания глобальной группы переводчиков создайте отдельные
# языковые группы, например translators-de, translators-fr, и назначьте им
# пользователей.
ROSETTA_LANGUAGE_GROUPS = False

ROSETTA_LOGIN_URL = LOGIN_URL

# Количество сообщений для отображения на странице
ROSETTA_MESSAGES_PER_PAGE = 10

ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'en'

ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'English'


ROSETTA_POFILENAMES = ('django.po', 'djangojs.po')

# Задает длину строки редактируемого PO-файла.
# Значение 0 - имитировать опцию makemessage --no-wrap
ROSETTA_POFILE_WRAP_WIDTH = 78

ROSETTA_REQUIRES_AUTH = True

# Добавляет удобную ссылку на Rosetta в нижней части индекса приложений
# администратора Django.
ROSETTA_SHOW_AT_ADMIN_PANEL = True

ROSETTA_SHOW_OCCURRENCES = True

ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'

ROSETTA_UWSGI_AUTO_RELOAD = False

ROSETTA_WSGI_AUTO_RELOAD = False

# Подключить перевод от Яндекса(Yandex.Translate API).
# Необходимо получить ключ AppID и указать его здесь.
YANDEX_TRANSLATE_KEY = None
