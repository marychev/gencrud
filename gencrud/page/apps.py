from django.apps import AppConfig
from gen.page.strings import BASE_PAGE_VERBOSE_NAME_PLURAL


class PageAppConfig(AppConfig):
    name = 'page'
    verbose_name = BASE_PAGE_VERBOSE_NAME_PLURAL

