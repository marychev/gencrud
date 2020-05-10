from django.http import HttpResponse
from gen.mixins import get_settings_template
from django.http import Http404


def robots_txt(request):
    if get_settings_template().robots_txt:
        return HttpResponse(get_settings_template().robots_txt)
    raise Http404
