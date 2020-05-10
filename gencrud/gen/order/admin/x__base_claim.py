# from django.contrib import admin
# from django.shortcuts import render
# from gen.abstract.admin import AbstractDefaultAdmin, AbstractCreatedAdmin
# from order.models.claim import FastClaim
#
#
# @admin.register(FastClaim)
# class BaseClaimAdmin(AbstractDefaultAdmin, AbstractCreatedAdmin):
#     search_fields = ('id', 'email', 'phone', 'fio')
#     actions = ('go_print',) + AbstractDefaultAdmin.actions
#     raw_id_fields = ('user',)
#
#     list_filter = ('status', 'typeof') + AbstractCreatedAdmin.list_filter
#     list_display = ('id', 'fio', 'email', 'phone', 'typeof', 'status')
#     list_display_links = ('id', 'fio')
#
#     readonly_fields = ('id',) + AbstractCreatedAdmin.readonly_fields
#
#     fieldsets = (
#         ('Основные данные', {
#             'classes': ('suit-tab', 'suit-tab-data'),
#             'fields': (
#                 ('id', 'status'), 'typeof',
#                 'user', 'fio', 'email', 'phone', 'created', 'updated',
#             )
#         }),
#     )
#
#     suit_form_tabs = (
#         ('data', 'ДАННЫЕ'),
#     )
#
#     def go_print(self, request, queryset):
#         """
#         Создать табличный вид объекта и выставить на печать
#         ? поля текщей модели обекта - заголовкок таблицы, и значения
#         ? Отдать сверстанную таблицу в ХТМЛ шаблон с кнопкой "Печать"
#         ? Кнопку обрабатывает JS 'print()' - вывести на печать
#         """
#         return render(request, 'order/go_print.html', context={'order': queryset.first()})
#     go_print.short_description = 'Распечатать'
#
