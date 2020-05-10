from django.db import models
from gen.order.models.abstract_claim import AbstractClaimModel
from gen.order.strings import BASE_CLAIM_VERBOSE_NAME, BASE_CLAIM_VERBOSE_NAME_PLURAL


class BaseClaimModel(AbstractClaimModel):
    class Meta:
        abstract = True
        verbose_name = BASE_CLAIM_VERBOSE_NAME
        verbose_name_plural = BASE_CLAIM_VERBOSE_NAME_PLURAL
        ordering = ('-created',)

    REQUEST = 0
    CALLER = 1
    TYPEOF_CHOICES = (
        (REQUEST, BASE_CLAIM_VERBOSE_NAME),
        (CALLER, 'Звонок')
    )

    fio = models.CharField(max_length=255, verbose_name='Ф.И.О')
    typeof = models.PositiveSmallIntegerField('Тип', choices=TYPEOF_CHOICES, default=CALLER)

    def __str__(self):
        return '{}: {}'.format(
            self.pk, self.get_typeof_display(),
        )



