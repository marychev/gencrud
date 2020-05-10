from django.contrib import admin
from site_info.models.list_link import ListLink
from gen.abstract.admin import AbstractDefaultAdmin


@admin.register(ListLink)
class BaseListLinkAdmin(AbstractDefaultAdmin):
    search_fields = ('title',)
    list_display = ('title', 'url', 'is_show', 'type_link')
    list_editable = ('type_link', 'url', 'is_show')
    list_filter = ('type_link', 'is_show')

