from django.contrib import admin
from django.shortcuts import render
from gen.abstract.admin import AbstractDefaultAdmin, AbstractCreatedAdmin
from order.models.fast_claim import FastClaim


@admin.register(FastClaim)
class BaseFastClaimAdmin(AbstractDefaultAdmin, AbstractCreatedAdmin):
    search_fields = ('id', 'email', 'phone')
    actions = ('go_print',) + AbstractDefaultAdmin.actions
    raw_id_fields = ('user',)

    list_filter = ('status', 'typeof') + AbstractCreatedAdmin.list_filter
    list_display = ('id', 'email', 'phone', 'typeof', 'status')
    list_display_links = ('id', 'email')

    readonly_fields = ('id',) + AbstractCreatedAdmin.readonly_fields

    fieldsets = (
        ('Основные данные', {
            'classes': ('suit-tab', 'suit-tab-data'),
            'fields': (
                ('id', 'status'), 'typeof',
                'user', 'email', 'phone', 'comment',
                'created', 'updated',
            )
        }),
    )

    suit_form_tabs = (
        ('data', 'ДАННЫЕ'),
    )

    def go_print(self, request, queryset):
        return render(request, 'order/go_print.html', context={'order': queryset.first()})
    go_print.short_description = 'Распечатать'

