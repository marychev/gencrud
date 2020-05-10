from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from site_info.models import SocialNetwork


@admin.register(SocialNetwork)
class BaseSocialNetworkAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    search_fields = ('title', 'image_title')
    list_display = AbstractImageAdmin.list_display + ('title', 'html_link', 'url')

