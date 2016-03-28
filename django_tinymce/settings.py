import os
from django.conf import settings


# def static_url(url):
#     return os.path.join(settings.STATIC_URL, url)

SETTINGS_DEFAULT = {
    'theme': 'simple',
    'relative_urls': False
}

SETTINGS_USER = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', 'filebrowser' in settings.INSTALLED_APPS)

tinymce_config = SETTINGS_DEFAULT.copy()
tinymce_config.update(SETTINGS_USER)
