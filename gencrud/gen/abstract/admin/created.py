from django.contrib import admin


class AbstractCreatedAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
    list_filter = ('created', 'updated')
