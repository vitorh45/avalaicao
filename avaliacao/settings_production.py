# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from settings import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'avaliacao',
#         'USER': 'avaliacao',
#         'PASSWORD': 'avaliacao',
#         'HOST': '',
#         'PORT': '',
#     }
# }

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
