from django.contrib import admin
from django.shortcuts import render
from gen.abstract.admin import AbstractDefaultAdmin, AbstractCreatedAdmin
from order.models import ProductClaim


@admin.register(ProductClaim)
class BaseProductClaimAdmin(AbstractDefaultAdmin, AbstractCreatedAdmin):
    search_fields = ('id', 'email', 'phone', 'product__title')
    actions = ('go_print',) + AbstractDefaultAdmin.actions
    raw_id_fields = ('user', 'product')

    list_filter = ('status', 'product') + AbstractCreatedAdmin.list_filter
    list_display = ('id', 'email', 'phone', 'product', 'status')
    list_display_links = ('id', 'email')
    filter_horizontal = ('product_items', )
    readonly_fields = ('id',) + AbstractCreatedAdmin.readonly_fields

    fieldsets = (
        ('Основные данные', {
            'classes': ('suit-tab', 'suit-tab-data'),
            'fields': (
                ('id', 'status'), 
                'product', 'product_items',
                'user', 'email', 'phone', 'comment',
                'created', 'updated',
            )
        }),
    )

    suit_form_tabs = (
        ('data', 'ДАННЫЕ'),
    )

    def go_print(self, request, queryset):
        """
        Создать табличный вид объекта и выставить на печать
        ? поля текщей модели обекта - заголовкок таблицы, и значения
        ? Отдать сверстанную таблицу в ХТМЛ шаблон с кнопкой "Печать"
        ? Кнопку обрабатывает JS 'print()' - вывести на печать
        """
        return render(request, 'order/go_print.html', context={'order': queryset.first()})
    go_print.short_description = 'Распечатать'

