from django.apps import AppConfig
from gen.catalog.strings import BASE_CATALOG_VERBOSE_NAME


class CatalogAppConfig(AppConfig):
    name = 'catalog'
    verbose_name = BASE_CATALOG_VERBOSE_NAME

