from django.db import models
from gen.param.string import (
    BASE_PARAM_VERBOSE_NAME, BASE_PARAM_VERBOSE_NAME_PLURAL,
    STR_TYPE, INT_TYPE, BOOL_TYPE, DECIMAL_TYPE, COLOR_TYPE)


class BaseParamModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = '{} (dev)'.format(BASE_PARAM_VERBOSE_NAME)
        verbose_name_plural = '{} (dev)'.format(BASE_PARAM_VERBOSE_NAME_PLURAL)
        ordering = ('typeof',)

    STR = 'string'
    INT = 'integer'
    BOOL = 'bool'
    DECIMAL = 'decimal'
    TYPEOF_CHOICES = (
        (STR, STR_TYPE),
        (INT, INT_TYPE),
        (BOOL, BOOL_TYPE),
        (DECIMAL, DECIMAL_TYPE),
    )

    DECOR_COLOR = 'color'
    DECOR_CHOICES = (
        (DECOR_COLOR, COLOR_TYPE),
    )

    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    typeof = models.CharField(verbose_name='Тип параметра', default=STR, choices=TYPEOF_CHOICES, max_length=8)
    decor = models.CharField(
        verbose_name='Оформление, тип отоброжения(в разработке)', choices=DECOR_CHOICES, max_length=8,
        blank=True, null=True)

    def __str__(self):
        return self.title

    def promo_auto_create_values(self):
        """
        #TODO: Параметры для создания объявления c Авто.
        :return qs: ParmValue for self
        """
        # temporal function!
        from param.models import ParamValue
        return ParamValue.objects.filter(param=self.pk)

    def values(self):
        """
        :return qs: ParmValue for self
        """
        from param.models import ParamValue
        return ParamValue.objects.filter(param=self.pk)
