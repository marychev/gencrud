from __future__ import unicode_literals
from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin
from order.models import Status


@admin.register(Status)
class BaseStatusAdmin(AbstractDefaultAdmin):
    search_fields = ('name',)
