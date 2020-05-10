from django.forms import widgets
from ..forms import CSS_CLASS_TEXT_INPUT


class DateInputWidget(widgets.DateInput):
    input_type = 'date'

    def get_context(self, name, value, attrs):
        context = super(DateInputWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = CSS_CLASS_TEXT_INPUT
        return context

