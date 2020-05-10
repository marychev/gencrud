from django.contrib import admin

from catalog.models import CatalogImage
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin


@admin.register(CatalogImage)
class BaseCatalogImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = ('catalog',)
    list_filter = ('catalog',) + AbstractImageAdmin.list_filter
    list_display = ('catalog',) + AbstractImageAdmin.list_display
