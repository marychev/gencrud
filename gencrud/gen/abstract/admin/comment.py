from gen.abstract.admin import AbstractCreatedAdmin


class AbstractCommentAdmin(AbstractCreatedAdmin):
    class Meta:
        abstract = True

    raw_id_fields = ('user',)
    search_fields = ('username', 'text')
    list_display = ('email', 'user', 'text', 'is_show', 'created')
    list_display_links = ('email', 'user')
    list_editable = ('is_show',)
    list_filter = ('is_show',) + AbstractCreatedAdmin.list_filter
