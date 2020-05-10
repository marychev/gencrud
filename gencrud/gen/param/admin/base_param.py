from django.contrib import admin
from gen.abstract.admin.default import AbstractDefaultTabularInlineAdmin
from param.models import Param, ParamValue


class ParamValueTabInline(AbstractDefaultTabularInlineAdmin):
    model = ParamValue


@admin.register(Param)
class BaseParamAdmin(admin.ModelAdmin):
    list_display = ('title', 'typeof')
    inlines = (ParamValueTabInline,)


