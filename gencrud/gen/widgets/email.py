from django.forms import widgets
from ..forms import CSS_CLASS_TEXT_INPUT


class EmailInputWidget(widgets.EmailInput):

    def get_context(self, name, value, attrs):
        context = super(EmailInputWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = CSS_CLASS_TEXT_INPUT
        return context

