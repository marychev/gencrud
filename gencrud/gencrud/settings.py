from gen.settings import *
from gen.settings_db import *
from gen.settings_ckeditor import *
from gen.settings_filebrowser import *
from gen.settings_easy_thumbnails import *
from settings import SITE_DOMAIN, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


DEBUG = True

# todo: generate custom key for a new install
SECRET_KEY = 'hph53g@p+i@q0me76#v)+6p&(xcc!)@e=oi8oum)lo_bethany'


PROTOCOL = 'https'
ALLOWED_HOSTS = ['www.{}'.format(SITE_DOMAIN), SITE_DOMAIN, 'localhost', '127.0.0.1']

# -- ONLY DURING DEVELOPMENT --
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # show to console
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = EMAIL_HOST_USER
# ------------------------------------------------------------------


