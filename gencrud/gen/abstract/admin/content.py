from django.contrib import admin


class AbstractContentAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    _fields = ('title', 'description', 'html', 'is_show', 'author', 'sort', 'tags', 'is_allow_comments')
    filter_horizontal = ('tags',)

    @staticmethod
    def fields_element():
        return (
            'content', {
                'classes': ('suit-tab', 'suit-tab-content',),
                'fields': AbstractContentAdmin._fields}
        )
