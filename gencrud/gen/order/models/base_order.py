from __future__ import unicode_literals
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from gen.abstract.models import AbstractCreatedModel
from gen.order.strings import BASE_ORDER_VERBOSE_NAME, BASE_ORDER_VERBOSE_NAME_PLURAL
from order.models.story import Story


class BaseOrderModel(AbstractCreatedModel):
    class Meta:
        abstract = True
        verbose_name = BASE_ORDER_VERBOSE_NAME
        verbose_name_plural = BASE_ORDER_VERBOSE_NAME_PLURAL
        ordering = ('-created', )

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='Город', null=True, blank=True)
    total_cost = models.DecimalField(
        verbose_name='Общая стоимость', max_digits=10, decimal_places=2,
        validators=[MinValueValidator(Decimal(0.00))],
        help_text=' Автоматический расчет при сохранении.')
    status = models.ForeignKey('order.Status', verbose_name='Статус заказа', null=True, on_delete=models.CASCADE)
    ttn = models.CharField('Товарно-транспортная накладная', blank=True, null=True, max_length=128)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return 'Заказ: {}'.format(self.pk)

    def get_user_full_name(self):
        full_name = '%s %s' % (self.last_name, self.first_name)
        if (self.first_name in self.user.first_name) and (self.last_name in self.user.last_name):
            full_name = self.user.get_full_name()
        return full_name

    def get_total_qty(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())

    def save(self, *args, **kwargs):
        if not self.total_cost:
            self.total_cost = self.get_total_cost()
        if self.pk:
            Story.create_or_update(order=self)

        super(BaseOrderModel, self).save(*args, *kwargs)



