from django.forms import widgets
from ..forms import CSS_CLASS_MODEL_CHOICES


class SelectWidget(widgets.Select):

    def get_context(self, name, value, attrs):
        context = super(SelectWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = CSS_CLASS_MODEL_CHOICES
        context['widget']['attrs']['placeholder'] = name.title()
        return context

