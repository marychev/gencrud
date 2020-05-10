from django.contrib import admin
from site_info.models import TextInfo
from gen.abstract.admin import AbstractDefaultAdmin


@admin.register(TextInfo)
class BaseTextInfoAdmin(AbstractDefaultAdmin):
    search_fields = ('title',)
    list_display = ('title', 'get_html')
    list_filter = ('title',)


