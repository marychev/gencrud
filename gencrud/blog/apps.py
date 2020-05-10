from django.apps import AppConfig
from gen.blog.strings import BASE_BLOG_VERBOSE_NAME, APP_NAME


class BlogAppConfig(AppConfig):
    name = APP_NAME
    verbose_name = BASE_BLOG_VERBOSE_NAME

