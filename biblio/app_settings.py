# -*- coding: utf-8 -*-
from django.conf import settings

GOOGLE_API_URL = getattr(settings, 'GOOGLE_API_URL', 'https://www.googleapis.com/books/v1/volumes')