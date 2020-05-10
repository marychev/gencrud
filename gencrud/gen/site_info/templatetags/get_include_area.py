from django import template
from django.template.loader import render_to_string
from django.conf import settings
from site_info.models import IncludeArea
from htmlmin.minify import html_minify


register = template.Library()


@register.simple_tag
def get_include_area(request, code, *args, **kwargs):
    """
    For example: `{% get_include_area request code='advantages' %}`
    """
    theme_templates = settings.TEMPLATES[0]['DIRS'][0]
    file_path = '{}/include_area/templates/{}.html'.format(theme_templates, code)
    try:
        include_areas = IncludeArea.objects.filter(code=code, is_show=True)
        return render_to_string(file_path, {'include_areas': include_areas})
    except IncludeArea.DoesNotExist:
        pass

