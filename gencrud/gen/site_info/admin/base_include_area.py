from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin
from gen.abstract.admin import AbstractImageAdmin
from site_info.models.include_area import IncludeArea
from gen.site_info.strings import APP_NAME


@admin.register(IncludeArea)
class BaseIncludeAreaAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    actions = AbstractDefaultAdmin.actions + AbstractImageAdmin.actions + ('set_fixtures', 'load_fixtures')
    search_fields = ('title', 'code')
    list_display = ('thumb', 'title', 'is_show', 'code', 'sort')
    list_display_links = ('thumb', 'title')
    list_editable = ('is_show', 'sort')
    list_filter = ('is_show', 'code')

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseIncludeAreaAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = 'Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseIncludeAreaAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = 'Фикстуры: Загрузить последние'
