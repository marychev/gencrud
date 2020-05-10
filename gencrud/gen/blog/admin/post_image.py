from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from blog.models import PostImage


@admin.register(PostImage)
class BasePostImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = ('post',)
    list_filter = ('post',) + AbstractImageAdmin.list_filter
    list_display = ('post',) + AbstractImageAdmin.list_display


