from gen.param.mixin.value import AbstractParamValueModel
from gen.param.string import BASE_VALUE_VERBOSE_NAME, BASE_VALUE_VERBOSE_NAME_PLURAL


class BaseParamValue(AbstractParamValueModel):
    class Meta:
        abstract = True
        verbose_name = BASE_VALUE_VERBOSE_NAME
        verbose_name_plural = BASE_VALUE_VERBOSE_NAME_PLURAL
