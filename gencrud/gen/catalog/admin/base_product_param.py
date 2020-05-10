from django.contrib import admin

from catalog.models import ProductParam
from gen.abstract.admin import AbstractDefaultAdmin


@admin.register(ProductParam)
class BaseProductParamAdmin(AbstractDefaultAdmin):
    raw_id_fields = ('product', 'param',)
