# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from settings import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'avaliacao',
        'USER': 'avaliacao',
        'PASSWORD': 'avaliacao',
        'HOST': '',
        'PORT': '',
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
