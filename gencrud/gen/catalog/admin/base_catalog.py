from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from catalog.models import Catalog, CatalogImage
from gen.abstract.admin import AbstractMPTTPageSeoAdmin, AbstractImageInlineAdmin
from gen.catalog.strings import APP_NAME


class CatalogResource(resources.ModelResource):
    class Meta:
        model = Catalog
        skip_unchanged = True
        report_skipped = False
        fields = (
            'id',
            'title', 'description', 'html',
            'seo_title', 'seo_description', 'seo_keywords',
            'is_show', 'sort',
            'parent__title'
        )
        export_order = (
            'id', 'title', 'description', 'html',
            'seo_title', 'seo_description', 'seo_keywords',
            'is_show', 'sort',
            'parent__title',
        )


class CatalogImageInline(AbstractImageInlineAdmin):
    model = CatalogImage


@admin.register(Catalog)
class BaseCatalogAdmin(ImportExportModelAdmin, AbstractMPTTPageSeoAdmin):
    resource_class = CatalogResource
    inlines = (CatalogImageInline,)
    actions = AbstractMPTTPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')

    fieldsets = (
        # fields_element(('parent',)),
        AbstractMPTTPageSeoAdmin.fieldsets[0],
        AbstractMPTTPageSeoAdmin.fieldsets[1],
        AbstractMPTTPageSeoAdmin.fieldsets[2],
        AbstractMPTTPageSeoAdmin.fieldsets[3],
    )

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseCatalogAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = '[не применять] Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseCatalogAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = '[не применять] Фикстуры: Загрузить последние'
