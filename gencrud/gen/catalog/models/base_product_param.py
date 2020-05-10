from django.db import models

from catalog.models.product import Product
from gen.catalog.strings import BASE_PRODUCT_PARAM_VERBOSE_NAME_PLURAL, BASE_PRODUCT_VERBOSE_NAME
from gen.param.mixin import AbstractParamValueModel


class BaseProductParamModel(AbstractParamValueModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PRODUCT_PARAM_VERBOSE_NAME_PLURAL
        verbose_name_plural = BASE_PRODUCT_PARAM_VERBOSE_NAME_PLURAL
        ordering = ('product', 'param')

    product = models.ForeignKey(
        Product, verbose_name=BASE_PRODUCT_VERBOSE_NAME, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}: {}'.format(str(self.product), str(self.param))
