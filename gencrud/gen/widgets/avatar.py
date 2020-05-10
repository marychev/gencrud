from string import Template
from django import forms
from django.utils.safestring import mark_safe


class AvatarWidget(forms.widgets.Widget):
    # TODO: [upgrade]
    def render(self, name, value, attrs=None, renderer=None):
        html = Template('''<img width="90%" src="/media/$link"/>''')
        return mark_safe(html.substitute(link=value))

