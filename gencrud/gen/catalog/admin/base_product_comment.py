from django.contrib import admin
from gen.abstract.admin import AbstractCommentAdmin
from catalog.models.product_comment import ProductComment


@admin.register(ProductComment)
class BaseProductCommentAdmin(AbstractCommentAdmin):
    raw_id_fields = AbstractCommentAdmin.raw_id_fields + ('product',)
    list_display = AbstractCommentAdmin.list_display + ('product',)
    list_filter = AbstractCommentAdmin.list_filter + ('product',)
