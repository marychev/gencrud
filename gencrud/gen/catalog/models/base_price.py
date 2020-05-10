from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from gen.abstract.models import AbstractTitleModel
from gen.catalog.strings import BASE_PRICE_VERBOSE_NAME
from gen.catalog.models.base_product_item import BaseProductItemModel


class BasePriceModel(AbstractTitleModel):
    class Meta:
        abstract = True
        unique_together = ('title', 'name', 'price', 'unit')
        ordering = ('title', 'price')
        verbose_name = BASE_PRICE_VERBOSE_NAME
        verbose_name_plural = BASE_PRICE_VERBOSE_NAME

    name = models.CharField(max_length=512, verbose_name='Расшифровка', blank=True, null=True)
    price = models.DecimalField(
        verbose_name='Цена', blank=True, null=True,
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal(0))])
    unit = models.CharField(
        max_length=3, verbose_name='Ед.изм',
        choices=BaseProductItemModel.UNIT_CHOICES, default=BaseProductItemModel.PCS)

