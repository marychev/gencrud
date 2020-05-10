from django.apps import AppConfig
from gen.home.strings import BASE_HOME_VERBOSE_NAME


class HomeAppConfig(AppConfig):
    name = 'home'
    verbose_name = BASE_HOME_VERBOSE_NAME
