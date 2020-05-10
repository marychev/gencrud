from django.contrib import admin
from gen.abstract.admin import AbstractImageAdmin, AbstractDefaultAdmin
from home.models.slider import SliderHome


@admin.register(SliderHome)
class BaseSliderHomeAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    search_fields = ('title',)
    list_display = ('thumb', 'title', 'description', 'url', 'sort')
    list_display_links = ('thumb', 'title')
    list_editable = ('sort',)
    list_filter = ('sort', )
