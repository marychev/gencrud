from django.db import models
from django.core.exceptions import ValidationError


class StrValueMixin(models.Model):
    class Meta:
        abstract = True

    str_value = models.CharField(max_length=255, verbose_name='Значение(строка)', blank=True, null=True)

    # @property
    # def value(self):
    #     return self.str_value

    def clean(self):
        from param.models.param import Param

        super().clean()

        error_msg = 'Значение должно быть только одно!{}'.format(self.typeof)
        validation = ValidationError(error_msg, code='invalid')

        if self.typeof == Param.STR and (
                self.int_value is not None or
                self.bool_value is not None or
                self.decimal_value is not None):
            raise validation


class IntValueMixin(models.Model):
    class Meta:
        abstract = True

    int_value = models.IntegerField(verbose_name='Значение(целое число)', blank=True, null=True)

    # @property
    # def value(self):
    #     return self.int_value

    def clean(self):
        from param.models.param import Param

        super().clean()

        error_msg = 'Значение должно быть только одно!{}'.format(self.typeof)
        validation = ValidationError(error_msg, code='invalid')
        if self.typeof == Param.INT and (
                self.decimal_value is not None or
                self.bool_value is not None or
                self.str_value is not None):
            raise validation


class DecimalValueMixin(models.Model):
    class Meta:
        abstract = True

    decimal_value = models.DecimalField(
        verbose_name='Значение(денежный формат)',
        max_digits=13, decimal_places=2, blank=True, null=True
    )

    @property
    def value(self):
        return self.decimal_value

    def clean(self):
        from param.models.param import Param

        super().clean()

        error_msg = 'Значение должно быть только одно!{}'.format(self.typeof)
        validation = ValidationError(error_msg, code='invalid')
        if self.typeof == Param.DECIMAL and (
                self.int_value is not None or
                self.bool_value is not None or
                self.str_value is not None):
            raise validation


class BoolValueMixin(models.Model):
    class Meta:
        abstract = True

    bool_value = models.NullBooleanField(max_length=255, verbose_name='Значение(булево)', blank=True, null=True)

    def clean(self):
        from param.models.param import Param

        super().clean()

        error_msg = 'Значение должно быть только одно!{}'.format(self.typeof)
        validation = ValidationError(error_msg, code='invalid')
        if self.value is not None and self.typeof == Param.BOOL and (
                self.int_value is not None or
                self.str_value is not None or
                self.decimal_value is not None):
            raise validation


class AbstractParamValueModel(StrValueMixin, IntValueMixin, DecimalValueMixin, BoolValueMixin):
    class Meta:
        abstract = True

    param = models.ForeignKey('param.Param', verbose_name='Параметр', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value())

    @property
    def typeof(self):
        return self.param.typeof

    def value(self):
        if self.int_value is not None:
            return self.int_value
        elif self.bool_value is not None:
            return self.bool_value
        elif self.decimal_value is not None:
            return self.decimal_value
        else:
            return self.str_value

    def set_typeof_value(self, val):
        from param.models import Param

        if self.typeof == Param.BOOL:
            self.bool_value = val
        elif self.typeof == Param.INT:
            self.int_value = val
        elif self.typeof == Param.DECIMAL:
            self.decimal_value = val
        else:
            self.str_value = val

