from django.forms import widgets
from ..forms import CSS_CLASS_TEXT_INPUT


class TextInputWidget(widgets.TextInput):
    def get_context(self, name, value, attrs):
        context = super(TextInputWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = CSS_CLASS_TEXT_INPUT
        return context


class TextareaWidget(widgets.Textarea):
    def get_context(self, name, value, attrs):
        context = super(TextareaWidget, self).get_context(name, value, attrs)
        context['widget']['attrs']['class'] = CSS_CLASS_TEXT_INPUT
        context['widget']['attrs']['rows'] = 4
        return context

