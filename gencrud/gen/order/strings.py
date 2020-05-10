APP_NAME = 'order'
BASE_CLAIM_VERBOSE_NAME = 'Заявка'
BASE_CLAIM_VERBOSE_NAME_PLURAL = 'Заявки'

BASE_PRODUCT_CLAIM_VERBOSE_NAME = '{}: товар'.format(BASE_CLAIM_VERBOSE_NAME)
BASE_PRODUCT_CLAIM_VERBOSE_NAME_PLURAL = '{}: товар'.format(BASE_CLAIM_VERBOSE_NAME_PLURAL)

BASE_STATUS_VERBOSE_NAME = 'Статус'
BASE_STATUS_VERBOSE_NAME_PLURAL = 'Статусы'

BASE_ORDER_VERBOSE_NAME = 'Заказ'
BASE_ORDER_VERBOSE_NAME_PLURAL = 'Заказы'

BASE_ORDER_STORY_VERBOSE_NAME = '{}: история'.format(BASE_ORDER_VERBOSE_NAME)

BASE_ORDER_ITEM_VERBOSE_NAME = '{}: пункт'.format(BASE_ORDER_VERBOSE_NAME)
BASE_ORDER_ITEM_VERBOSE_NAME_PLURAL = '{}: пункты'.format(BASE_ORDER_VERBOSE_NAME)