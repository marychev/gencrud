from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin
from catalog.models.price import Price


@admin.register(Price)
class BasePriceAdmin(AbstractDefaultAdmin):
    search_fields = ('title', 'name', 'description')
    list_display = ('pk', 'description', 'title', 'price', 'unit', 'name')
    list_display_links = ('pk', 'description')
    list_filter = ('unit', 'price')
    fields = ('description', 'title', 'price', 'unit', 'name')
