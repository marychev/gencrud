from decimal import Decimal

from django.db import models
from django.urls import reverse

from catalog.models import Catalog
from catalog.models.product_comment import ProductComment
from catalog.models.product_image import ProductImage
from catalog.models.product_item import ProductItem
from gen.abstract.models import AbstractPageSeoModel
from gen.catalog.strings import (
    BASE_CATALOG_VERBOSE_NAME, BASE_PRODUCT_VERBOSE_NAME, BASE_PRODUCT_VERBOSE_NAME_PLURAL)
from gen.utils.price import format_price


class BaseProductModel(AbstractPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PRODUCT_VERBOSE_NAME
        verbose_name_plural = BASE_PRODUCT_VERBOSE_NAME_PLURAL
        unique_together = ('title', 'slug')

    DEFAULT_LAYOUT = 'product/templates/product_detail.html'
    IMAGES_MIN_BOTTOM_LAYOUT = 'product/templates/product_detail_layout_images_min_bottom.html'
    LAYOUTS = (
        (DEFAULT_LAYOUT, 'Шаблон по умолчанию'),
        (IMAGES_MIN_BOTTOM_LAYOUT, 'Шаблон: мини-изображения под главной фотографией')
    )

    articul = models.CharField(max_length=256, verbose_name='Артикул (уник)', db_index=True, blank=True, null=True)
    catalogs = models.ManyToManyField(
        Catalog, blank=True, verbose_name=BASE_CATALOG_VERBOSE_NAME,
        limit_choices_to={'is_show': True},
    )
    is_bestseller = models.BooleanField(default=False, verbose_name='Хит продаж')
    is_new = models.BooleanField(default=True, verbose_name='Новинка')
    recommend_products = models.ManyToManyField(
        'self', verbose_name='Рекомендованные/Похожие', blank=True, limit_choices_to={'is_show': True},
        help_text='Отображаются внизу карточки товара, как рекомендованные или похожие товары')
    layout = models.CharField(
        max_length=256, choices=LAYOUTS, default=DEFAULT_LAYOUT, verbose_name='Шаблоны страницы')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if 'CLONE' in self.title or 'CLONE' in self.slug:
            self.is_show = False
        super(BaseProductModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if ProductImage.objects.filter(product=self).first():
            [image.delete() for image in ProductImage.objects.filter(product=self)]
        if self.get_main_image():
            self.get_main_image().image.delete()
        super(BaseProductModel, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        catalog_slug = '#'
        if self.catalogs.first():
            catalog_slug = self.catalogs.first().slug
            return reverse('product_detail', args=[catalog_slug, self.slug])
        else:
            return catalog_slug

    def get_main_item(self):
        return ProductItem.objects.filter(product_id=self.id, is_main=True).first() or self.productitem_set.first()

    def get_price(self):
        price = 0
        if self.get_main_item() and self.get_main_item().price:
            price = Decimal(self.get_main_item().price)
        return price

    def get_price_format(self):
        return format_price(self.get_price())

    def get_price_discount(self):
        price = 0
        if self.get_main_item() and self.get_main_item().price_discount:
            price = Decimal(self.get_main_item().price_discount)
        return price

    def get_images(self):
        return ProductImage.objects.filter(product_id=self.pk)

    def get_comments(self):
        return ProductComment.objects.filter(product_id=self.pk, is_show=True)

    def get_product_items(self):
        return ProductItem.objects.filter(product_id=self.pk)

    def get_product_params(self):
        from catalog.models.product_param import ProductParam
        return ProductParam.objects.filter(product_id=self.pk)
