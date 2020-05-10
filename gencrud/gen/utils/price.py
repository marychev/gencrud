import locale
from decimal import Decimal


def format_price(price):
    """
    format_price(123456789.123)   # 123 456 789,12 ₽
    formats: en_US.UTF-8, ru_RU.UTF-8
    """
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return locale.currency(price, grouping=True)
    except locale.Error:
        # todo: [test] has troubles with tests on Pipelines
        return str(Decimal(price))


