from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from home.models import HomeImage


@admin.register(HomeImage)
class BaseHomeImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    pass
