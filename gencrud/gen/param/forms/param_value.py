from django.forms import ModelForm
from param.models.value import ParamValue


class CreatePromoParamValueForm(ModelForm):

    class Meta:
        model = ParamValue
        fields = '__all__'
