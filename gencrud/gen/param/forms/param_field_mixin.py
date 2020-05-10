from django import forms
from django.forms import widgets
from gen.forms import (
    CSS_CLASS_MODEL_CHOICES, CSS_CLASS_TEXT_INPUT
)


class ParamFieldMixin(forms.Form):
    def init_one_bool_field(self, param, required=True):
        self.fields['param_' + str(param.pk)] = forms.BooleanField(
            required=required,
            label=param.title,
            widget=widgets.CheckboxInput(),
        )

    def init_one_int_field(self, param, required=True):
        self.fields['param_' + str(param.pk)] = forms.IntegerField(
            required=required,
            label=param.title,
            widget=widgets.NumberInput(attrs={
                'class': CSS_CLASS_TEXT_INPUT,
                'placeholder': param.title,
            }),
        )

    def init_one_decimal_field(self, param, required=True):
        self.fields['param_' + str(param.pk)] = forms.DecimalField(
            required=required,
            label=param.title,
            widget=widgets.NumberInput(attrs={
                'class': CSS_CLASS_TEXT_INPUT,
                'placeholder': param.title
            }),
        )

    def init_one_str_field(self, param, required=True):
        self.fields['param_' + str(param.pk)] = forms.CharField(
            required=required,
            label=param.title,
            widget=widgets.TextInput(attrs={
                'class': CSS_CLASS_TEXT_INPUT,
                'placeholder': param.title
            }),
        )

    def init_selected_field(self, param, required=True):
        self.fields['param_' + str(param.pk)] = forms.ModelChoiceField(
            required=required,
            empty_label=':'+param.title,
            label=param.title,
            queryset=param.values(),
            widget=widgets.Select(attrs={'class': CSS_CLASS_MODEL_CHOICES})
        )
