from django.contrib import admin

from catalog.models.product_image import ProductImage
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin


@admin.register(ProductImage)
class BaseProductImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = ('product',)
    list_filter = ('product',) + AbstractImageAdmin.list_filter
    list_display = ('product',) + AbstractImageAdmin.list_display



