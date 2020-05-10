from django.contrib import admin

from gen.abstract.admin import AbstractCommentAdmin
from page.models.page_comment import PageComment


@admin.register(PageComment)
class BasePageCommentAdmin(AbstractCommentAdmin):
    raw_id_fields = AbstractCommentAdmin.raw_id_fields + ('page',)
    list_display = AbstractCommentAdmin.list_display + ('page',)
    list_filter = AbstractCommentAdmin.list_filter + ('page',)
