from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'server.lhy.kr',
    '.elasticbeanstalk.com',
]
WSGI_APPLICATION = 'config.wsgi.local.application'

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
