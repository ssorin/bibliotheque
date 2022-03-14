# -*- coding: utf-8 -*-
from core.settings import *

ALLOWED_HOSTS = []
DEBUG = True


# ==============================================================================
# Database configuration
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
