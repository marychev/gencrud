from django.contrib import admin
from gen.abstract.admin import AbstractMPTTPageSeoAdmin, AbstractImageInlineAdmin, fields_element
from blog.models import Blog, BlogImage


class BlogImageInline(AbstractImageInlineAdmin):
    model = BlogImage


@admin.register(Blog)
class BaseBlogAdmin(AbstractMPTTPageSeoAdmin):
    inlines = (BlogImageInline,)
    actions = AbstractMPTTPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')

    fieldsets = (
        fields_element(('parent',)),
        AbstractMPTTPageSeoAdmin.fieldsets[0],
        AbstractMPTTPageSeoAdmin.fieldsets[2],
        AbstractMPTTPageSeoAdmin.fieldsets[3],
    )
