from mptt.admin import MPTTModelAdmin
from .default import AbstractDefaultAdmin
from .created import AbstractCreatedAdmin
from .seo import AbstractSEOAdmin
from .content import AbstractContentAdmin
from .image import AbstractImageAdmin


def fields_element(fields):
    return ('Элементы объекта', {
        'classes': ('suit-tab', 'suit-tab-fields'),
        'fields': fields,
    })


def info_fieldsets_item(readonly_fields):
    return ('ИНФО', {
        'classes': ('suit-tab', 'suit-tab-info',),
        'fields': readonly_fields,
    })


class AbstractPageSeoAdmin(AbstractDefaultAdmin, AbstractContentAdmin, AbstractSEOAdmin,
                           AbstractImageAdmin, AbstractCreatedAdmin):
    class Meta:
        abstract = True

    search_fields = ('title',)
    readonly_fields = AbstractImageAdmin.readonly_fields + AbstractCreatedAdmin.readonly_fields
    raw_id_fields = ('author',)
    list_filter = ('is_show', 'is_allow_comments',  'tags', 'created', 'updated')
    list_display = ('thumb', 'title', 'slug', 'is_show', 'is_allow_comments', 'sort', 'created')  # 'get_html'
    list_display_links = ('thumb', 'title',)
    list_editable = ('sort', 'is_show', 'is_allow_comments')

    fieldsets = (
        AbstractContentAdmin.fields_element(),
        ('Элементы объекта', {
            'classes': ('suit-tab', 'suit-tab-fields'),
            'fields': (None,),
        }),
        AbstractSEOAdmin.fields_element(),
        info_fieldsets_item(readonly_fields),
    )

    suit_form_tabs = (
        ('content', 'КОНТЕНТ'),
        ('fields', 'ПОЛЯ'),
        ('seo', 'СЕО'),
        ('image', 'ФОТО'),
        ('info', 'ИНФО'),
    )


class AbstractMPTTPageSeoAdmin(MPTTModelAdmin, AbstractPageSeoAdmin):
    class Meta:
        abstract = True

    mptt_level_indent = 23
    actions = ('rebuild',) + AbstractPageSeoAdmin.actions
    raw_id_fields = ('parent',) + AbstractPageSeoAdmin.raw_id_fields
    list_filter = ('parent',) + AbstractPageSeoAdmin.list_filter
    list_display = ('parent',) + AbstractPageSeoAdmin.list_display
    list_display_links = ('parent',) + AbstractPageSeoAdmin.list_display_links

    fieldsets = (
        AbstractPageSeoAdmin.fieldsets[0],
        fields_element(('parent',)),
        AbstractPageSeoAdmin.fieldsets[2],
        AbstractPageSeoAdmin.fieldsets[3],
    )

    def rebuild(self, request, queryset):
        self.model.objects.rebuild()
    rebuild.short_description = 'Пересобрать пункты раздела'
