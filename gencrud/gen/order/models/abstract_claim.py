from django.db import models
from gen.abstract.models import AbstractCreatedModel
from django.contrib.auth.models import User


class AbstractClaimModel(AbstractCreatedModel):
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Телефон', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey('order.Status', verbose_name='Статус', null=True, on_delete=models.SET_NULL)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(
            self.pk, self.get_typeof_display(),
        )

    class Meta:
        abstract = True

