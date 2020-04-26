#! coding: utf-8

from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbp',
        'USER': 'dbp',
        'PASSWORD': '12345',
        'HOST': '0.0.0.0',
        'PORT': 5432,
    }
}
