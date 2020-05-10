from __future__ import unicode_literals
from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from gen.abstract.admin.default import AbstractDefaultAdmin
from order.models.story import Story


@admin.register(Story)
class BaseStoryAdmin(AbstractDefaultAdmin):
    date_hierarchy = 'created'
    search_fields = ('order_id', 'status')
    list_filter = (
        'status',
        'created'
        # ('created', DateRangeFilter),
    )
    list_display = ('order', 'status', 'total_cost', 'created', 'comment')
    raw_id_fields = ('order',)
