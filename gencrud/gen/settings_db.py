import os
import sys
from gen.settings import BASE_DIR
from settings import DB_NAME, DB_USER, DB_PASSWORD


# ------------
# - postgres -
# ------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASSWORD,
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
# ---------------------------------------------------------

# ------------
# - sqlite3 -
# ------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{}/{}.db'.format(os.path.join(BASE_DIR, '..', 'theme'), DB_NAME),
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_{}'.format(DB_NAME)
    }
# ---------------------------------------------------------
