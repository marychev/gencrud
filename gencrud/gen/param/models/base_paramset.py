from django.db import models
from param.models.param import Param
from gen.param.string import (
    BASE_PARAMSET_VERBOSE_NAME, BASE_PARAMSET_VERBOSE_NAME_PLURAL,
    BASE_PARAM_VERBOSE_NAME_PLURAL)


class BaseParamSetModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_PARAMSET_VERBOSE_NAME + ' (dev)'
        verbose_name_plural = BASE_PARAMSET_VERBOSE_NAME_PLURAL + ' (dev)'
        ordering = ('typeof',)

    PROMO_CREATE_AUTO = 0
    PROMO_HOME_FILTER = 1
    TYPEOF_CHOICES = (
        (PROMO_CREATE_AUTO, 'Новое объявление: автомобиль'),
        (PROMO_HOME_FILTER, 'Фильтр для главной страницы: объявления'),
    )

    typeof = models.PositiveSmallIntegerField(verbose_name='Тип', choices=TYPEOF_CHOICES, unique=True)
    params = models.ManyToManyField(Param, verbose_name=BASE_PARAM_VERBOSE_NAME_PLURAL, blank=True)

    def __str__(self):
        return self.get_typeof_display()

    @staticmethod
    def promo_create_auto():
        return BaseParamSetModel.objects.get(
            typeof=BaseParamSetModel.PROMO_CREATE_AUTO).params.all().order_by('id')

    @staticmethod
    def promo_home_filter():
        return BaseParamSetModel.objects.get(
            typeof=BaseParamSetModel.PROMO_HOME_FILTER).params.all().order_by('id')
