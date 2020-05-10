from django.db import models

from catalog.models import Product, ProductItem
from gen.catalog.strings import (BASE_PRODUCT_VERBOSE_NAME, BASE_PRODUCT_ITEM_VERBOSE_NAME)
from gen.order.models.abstract_claim import AbstractClaimModel
from gen.order.strings import BASE_PRODUCT_CLAIM_VERBOSE_NAME, BASE_PRODUCT_CLAIM_VERBOSE_NAME_PLURAL


class BaseProductClaimModel(AbstractClaimModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PRODUCT_CLAIM_VERBOSE_NAME
        verbose_name_plural = BASE_PRODUCT_CLAIM_VERBOSE_NAME_PLURAL
        ordering = ('-created',)

    product = models.ForeignKey(Product, verbose_name=BASE_PRODUCT_VERBOSE_NAME, on_delete=models.CASCADE)
    product_items = models.ManyToManyField(ProductItem, verbose_name=BASE_PRODUCT_ITEM_VERBOSE_NAME, blank=True)

    def __str__(self):
        return '# {}: {}'.format(self.pk, self.product)

    @staticmethod
    def get_form():
        from gen.order.forms import ProductClaimForm
        return ProductClaimForm
