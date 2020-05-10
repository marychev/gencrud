from django.db import models
from gen.order.models.abstract_claim import AbstractClaimModel
from gen.order.strings import BASE_CLAIM_VERBOSE_NAME, BASE_CLAIM_VERBOSE_NAME_PLURAL


class BaseFastClaimModel(AbstractClaimModel):
    class Meta:
        abstract = True
        verbose_name = BASE_CLAIM_VERBOSE_NAME
        verbose_name_plural = BASE_CLAIM_VERBOSE_NAME_PLURAL
        ordering = ('-created',)

    CALL = 0
    REQUEST_PROJECT = 1
    OTHER = 2
    TYPEOF_CHOICES = (
        (CALL, 'Позвони мне'),
        (REQUEST_PROJECT, 'Заявка на проект'),
        (OTHER, 'Другое')
    )

    typeof = models.PositiveSmallIntegerField('Тип', choices=TYPEOF_CHOICES, default=REQUEST_PROJECT)

    def __str__(self):
        return '{}: {}'.format(
            self.pk, self.get_typeof_display(),
        )

    @staticmethod
    def get_form():
        from gen.order.forms import FastClaimForm
        return FastClaimForm

