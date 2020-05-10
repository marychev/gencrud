import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENCRUD_LIBS = [
    'gen.suit',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'daterange_filter',
    'easy_thumbnails',
    'image_cropping',
    'import_export',
    'rest_framework',
]

GENCRUD_MODULES = [
    'gen.cart',
    'gen.search',
    'gen.utils',
]

GENCRUD_APPS = [
    'blog',
    'task',
    'catalog',
    'param',
    # todo: dev version
    # -- 'filter',
    'order',
    'users',
    'home',
    'page',
    'site_info',
    'settings_template',
]

INSTALLED_APPS = GENCRUD_LIBS + GENCRUD_MODULES + GENCRUD_APPS


ROOT_URLCONF = 'gencrud.urls'
WSGI_APPLICATION = 'gencrud.wsgi.application'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '..', 'theme', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'get_include_area': 'gen.site_info.templatetags.get_include_area',
            }
        },

    },
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'gencrud', 'static'),
    os.path.join(BASE_DIR, '..', 'app', 'static'))
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'theme', 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder')

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/stylus', 'stylus -u nib < {infile} > {outfile}'))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'theme', 'media')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
LOGIN_URL = '/users/login/'
CART_SESSION_ID = 'cart'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True

SITE_ID = 1
