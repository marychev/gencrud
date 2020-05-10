from __future__ import unicode_literals
from django.contrib import admin
from django.shortcuts import render
from gen.abstract.admin import AbstractDefaultAdmin, AbstractCreatedAdmin
from order.models import Order, OrderItem, Story


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product_item', )
    suit_classes = 'suit-tab suit-tab-product'
    extra = 0


class StoryInline(admin.TabularInline):
    model = Story
    readonly_fields = ('total_cost', 'status', 'comment', 'created')
    extra = 0
    suit_classes = 'suit-tab suit-tab-story'
    # закоментровать когда в продакшен уйдет -
    can_delete = None
    ordering = ('-id',)


@admin.register(Order)
class BaseOrderAdmin(AbstractDefaultAdmin, AbstractCreatedAdmin):
    search_fields = ('id', 'email', 'last_name')
    inlines = (OrderItemInline, StoryInline)
    actions = ('go_print',) + AbstractDefaultAdmin.actions + ('set_fixtures', 'load_fixtures')
    raw_id_fields = ('user',)
    list_filter = ('status', 'city') + AbstractCreatedAdmin.list_filter
    list_display = ('id', 'user', 'email', 'city', 'total_cost', 'status', 'created')
    list_display_links = ('id', 'user')
    readonly_fields = ('id', 'total_cost') + AbstractCreatedAdmin.readonly_fields

    fieldsets = (
        ('Основные данные', {
            'classes': ('suit-tab', 'suit-tab-data'),
            'fields': (
                ('id', 'status'), 'total_cost', 'user', 'last_name', 'first_name',
                'address', 'postal_code', 'city', 'ttn', 'comment', 'created', 'updated',
            )
        }),
    )

    suit_form_tabs = (
        ('data', 'ДАННЫЕ'),
        ('product', 'ЦЕНЫ/ТОВАРЫ'),
        ('story', 'ИСТОРИЯ'),
    )

    def go_print(self, request, queryset):
        """
        Создать табличный вид объекта и выставить на печать
        ? поля текщей модели обекта - заголовкок таблицы, и значения
        ? Отдать сверстанную таблицу в ХТМЛ шаблон с кнопкой "Печать"
        ? Кнопку обрабатывает JS 'print()' - вывести на печать
        """
        return render(request, 'order/templates/go_print.html', context={'order': queryset.first()})
    go_print.short_description = 'Распечатать'

