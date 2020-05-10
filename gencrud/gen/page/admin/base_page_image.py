from django.contrib import admin

from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from page.models.page_image import PageImage


@admin.register(PageImage)
class BasePageImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = ('page',)
    search_fields = ('image_title', 'page__title')
    list_display = AbstractImageAdmin.list_display + ('page',)
