from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from blog.models import BlogImage


@admin.register(BlogImage)
class BaseBlockImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = ('blog',)
    list_filter = ('blog',) + AbstractImageAdmin.list_filter
    list_display = ('blog',) + AbstractImageAdmin.list_display


