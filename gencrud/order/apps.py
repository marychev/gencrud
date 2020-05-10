from django.apps import AppConfig
from gen.order.strings import BASE_ORDER_VERBOSE_NAME


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = BASE_ORDER_VERBOSE_NAME


