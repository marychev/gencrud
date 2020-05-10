from gen.param.forms.param_field_mixin import ParamFieldMixin
from param.models import Param, ParamSet


class MainPromoFilterForm(ParamFieldMixin):
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)

        super(MainPromoFilterForm, self).__init__(*args, **kwargs)

        for param in ParamSet.promo_home_filter():
            if param.values().exists():
                self.init_selected_field(param, required=False)
            else:
                if param.typeof == Param.STR:
                    self.init_one_str_field(param, required=False)
                elif param.typeof == Param.DECIMAL:
                    self.init_one_decimal_field(param, required=False)
                elif param.typeof == Param.INT:
                    self.init_one_decimal_field(param, required=False)
                elif param.typeof == Param.BOOL:
                    self.init_one_bool_field(param, required=False)
