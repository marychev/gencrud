from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from gen.abstract.models import AbstractCreatedModel
from gen.catalog.strings import (
    BASE_PRODUCT_VERBOSE_NAME, BASE_PRODUCT_ITEM_VERBOSE_NAME, BASE_PRODUCT_ITEM_VERBOSE_NAME_PLURAL,
    TAKE_FROM_PRICE)


class BaseProductItemModel(AbstractCreatedModel):
    class Meta:
        abstract = True
        unique_together = ('product', 'name')
        ordering = ('product', '-is_main', 'name')
        verbose_name = BASE_PRODUCT_ITEM_VERBOSE_NAME
        verbose_name_plural = BASE_PRODUCT_ITEM_VERBOSE_NAME_PLURAL

    PCS = 'pcs'
    M = 'm'
    SQM = 'sqm'
    CBM = 'cbm'
    NOT_SHOW = 'not_show'
    UNIT_CHOICES = (
        (PCS, 'шт.'),
        (M, 'п.м'),
        (SQM, 'м.кв'),
        (CBM, 'м.куб'),
        (NOT_SHOW, ' - ')
    )

    product = models.ForeignKey('catalog.Product', verbose_name=BASE_PRODUCT_VERBOSE_NAME, on_delete=models.CASCADE)
    name = models.CharField(max_length=512, verbose_name='Наименование')
    text = models.CharField(max_length=510, verbose_name='Дополнительно', blank=True, null=True)
    unit = models.CharField(max_length=3, verbose_name='Ед.изм', choices=UNIT_CHOICES, default=PCS)
    price = models.DecimalField(
        verbose_name='Цена', blank=True, null=True,
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    price_discount = models.DecimalField(
        verbose_name='Акционная цена', blank=True, null=True,
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0'))],
        help_text='Если указана - станет `Ценой` товара')
    is_main = models.BooleanField(default=False, verbose_name='Главный')
    default_price = models.ForeignKey(
        'catalog.Price', verbose_name=TAKE_FROM_PRICE,
        null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.set_main()

        if (not self.price and not self.text) and self.default_price:
            self.price = self.default_price.price
            self.name = self.default_price.title
            self.text = self.default_price.name
            self.unit = self.default_price.unit

        if self.price_discount and not self.price:
            self.price = self.price_discount

        super(BaseProductItemModel, self).save(*args, **kwargs)

    def get_price(self):
        return self.price

    def set_main(self):
        if self.product.productitem_set.filter(is_main=True).count() >= 1:
            self.is_main = False
        elif self.product.productitem_set.filter(is_main=True).count() == 0:
            self.is_main = True
