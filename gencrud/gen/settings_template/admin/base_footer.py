from django.contrib import admin
from settings_template.models import Footer
from gen.abstract.admin import AbstractDefaultAdmin


@admin.register(Footer)
class BaseFooterAdmin(AbstractDefaultAdmin):
    radio_fields = {'text_info': admin.VERTICAL}
    filter_horizontal = ('list_link', 'catalog', 'page', 'blogs',)
    search_fields = ('title',)
    list_display = ('title', 'is_show', 'text_info')
    list_editable = ('is_show',)
    list_filter = (
        'is_show', 'list_link', 'text_info', 'page', 'catalog',
    )

    fieldsets = (
        ('Основные данные и настройки сайта', {
            'classes': ('suit-tab', 'suit-tab-data'),
            'fields': ('title', 'is_show',),
        }),
        ('Подключение элементов к шаблону', {
            'fields': ('catalog', 'page', 'blogs'),
            'classes': ('suit-tab', 'suit-tab-include'),
        }),
        ('Дополнительные элементы для футера', {
            'fields': ('text_info', 'list_link'),
            'classes': ('suit-tab', 'suit-tab-more'),
        }),
    )

    suit_form_tabs = (
        ('data', 'ДАННЫЕ САЙТА'),
        ('include', 'ПОДКЛЮЧЕНИЕ'),
        ('more', 'ДОПОЛНИТЕЛЬНО'),
    )

    def clone_object(self, request, queryset): pass
    clone_object.short_description = 'Клонировать: недоступно!'
