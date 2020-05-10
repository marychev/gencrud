from django.apps import AppConfig
from gen.settings_template.strings import BASE_SETTINGS_TEMPLATE_VERBOSE_NAME


class SettingsTemplateAppConfig(AppConfig):
    name = 'settings_template'
    verbose_name = BASE_SETTINGS_TEMPLATE_VERBOSE_NAME
