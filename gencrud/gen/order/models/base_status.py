from django.db import models
from gen.order.strings import BASE_STATUS_VERBOSE_NAME, BASE_STATUS_VERBOSE_NAME_PLURAL


class BaseStatusModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_STATUS_VERBOSE_NAME
        verbose_name_plural = BASE_STATUS_VERBOSE_NAME_PLURAL

    name = models.CharField(max_length=255, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.name
