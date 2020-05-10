from django import template
from gencrud.urls import CATALOG_APP

register = template.Library()


@register.filter
def url_handler(obj, name=CATALOG_APP):
    if CATALOG_APP in name:
        return obj.get_absolute_url()
    elif 'mainmenu' in name:
        if obj.blog:
            return obj.blog.get_absolute_url()
        elif obj.page:
            return obj.page.get_absolute_url()
        elif obj.catalog:
            return obj.catalog.get_absolute_url()
        return '/'

    return '/'
