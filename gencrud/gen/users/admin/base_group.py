from django.contrib import admin
from django.contrib.auth.models import Group
from gen.abstract.admin import AbstractDefaultAdmin

admin.site.unregister(Group)


@admin.register(Group)
class BaseGroupAdmin(AbstractDefaultAdmin):
    search_fields = ('name', 'permissions__name')
    list_filter = ('permissions', )
    filter_horizontal = ('permissions',)
