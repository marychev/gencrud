from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractCreatedAdmin
from gen.abstract.mixins.clone import CloneObjectMixin
from catalog.models.product_item import ProductItem


@admin.register(ProductItem)
class BaseProductItemAdmin(AbstractDefaultAdmin, AbstractCreatedAdmin):
    raw_id_fields = ('product', 'default_price', )
    search_fields = ('name', 'product__title')
    list_display = ('name', 'product', 'default_price',)
    list_display_links = ('name', 'product')
    list_filter = ('product__catalogs', ) + AbstractCreatedAdmin.list_filter

    def clone_object(self, request, queryset):
        [self._clone_object(request, obj) for obj in queryset]
    clone_object.short_description = CloneObjectMixin.action_name

    def _clone_object(self, request, obj):
        clone = obj
        clone.id = None
        clone.name = self.clone_format(obj.nane)
        clone.save()
        self.clone_success(request, obj)
