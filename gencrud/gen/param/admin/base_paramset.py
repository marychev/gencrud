from django.contrib import admin
from gen.abstract.admin.default import AbstractDefaultAdmin
from param.models import ParamSet


@admin.register(ParamSet)
class BaseParamSetAdmin(AbstractDefaultAdmin):
    filter_horizontal = ('params',)

