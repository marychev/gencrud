from django.apps import AppConfig
from gen.param.string import BASE_PARAM_VERBOSE_NAME_PLURAL


class ParamConfig(AppConfig):
    name = 'param'
    verbose_name = BASE_PARAM_VERBOSE_NAME_PLURAL
