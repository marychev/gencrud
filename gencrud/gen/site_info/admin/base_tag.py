from django.contrib import admin
from site_info.models import Tag
from gen.abstract.admin import AbstractDefaultAdmin


@admin.register(Tag)
class BaseTagAdmin(AbstractDefaultAdmin):
    pass


