import os


# Относительный путь от вашего параметра MEDIA_ROOT,
# в котором Photologue будет сохранять файлы изображений. 
PHOTOLOGUE_DIR = 'photologue'

# Ограничение по умолчанию для галереи.
PHOTOLOGUE_GALLERY_LATEST_LIMIT = None

# Количество случайных изображений из галереи для отображения.
PHOTOLOGUE_GALLERY_SAMPLE_SIZE = 5

# Параметр max_length для поля ImageModel ImageField
PHOTOLOGUE_IMAGE_FIELD_MAX_LENGTH = 100

# Размер буфера файла изображения.
PHOTOLOGUE_MAXBLOCK = 256 * 2 ** 10

# Photologue может интегрировать галереи и фотографии с фреймворком сайта
# Django. По умолчанию эта функция отключена, а новые галереи и фотографии
# автоматически привязываются к текущему сайту (SITE_ID = 1).
PHOTOLOGUE_MULTISITE = False

# Найдите пользовательскую функцию для определения путей к файлам. Указывает
# “вызываемый”, который принимает экземпляр модели и исходное загруженное имя
# файла и возвращает относительный путь из вашего MEDIA_ROOT, по которому
# будет сохранен файл. Эту функцию можно установить непосредственно.
PHOTOLOGUE_PATH = None

#Путь к образцу изображения
PHOTOLOGUE_SAMPLE_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'res', 'sample.jpg')