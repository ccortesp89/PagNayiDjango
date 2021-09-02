import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql10433963',
        'HOST': 'sql10.freesqldatabase.com',
        'USER': 'sql10433963',
        'PASSWORD': 'jPdtYgcVLQ',
        'PORT': 3306,
    }
}

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}