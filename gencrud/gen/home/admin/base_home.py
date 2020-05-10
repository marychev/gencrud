from django.contrib import admin
from gen.abstract.admin import (AbstractPageSeoAdmin, AbstractImageInlineAdmin, fields_element)
from home.models import (Home, HomeImage)
from gen.home.strings import APP_NAME


class HomeImageInline(AbstractImageInlineAdmin):
    model = HomeImage


@admin.register(Home)
class BaseHomeAdmin(AbstractPageSeoAdmin):
    inlines = (HomeImageInline,)
    actions = AbstractPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')
    raw_id_fields = AbstractPageSeoAdmin.raw_id_fields + ('blog',)
    list_filter = AbstractPageSeoAdmin.list_filter + ('blog',)
    filter_horizontal = ('catalogs',)

    fieldsets = (
        fields_element(('blog', 'catalogs', 'video')),              # fields
        AbstractPageSeoAdmin.fieldsets[0],      # content
        AbstractPageSeoAdmin.fieldsets[2],      # seo
        AbstractPageSeoAdmin.fieldsets[3],      # info + ...inline
    )

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = '[не применять] Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = '[не применять] Фикстуры: Загрузить последние'



