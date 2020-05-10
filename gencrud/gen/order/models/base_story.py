from __future__ import unicode_literals
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from gen.order.strings import BASE_STATUS_VERBOSE_NAME


class BaseStoryModel(models.Model):
    class Meta:
        abstract = True
        unique_together = ('order', 'status', 'total_cost')
        verbose_name = 'Заказ:История'
        verbose_name_plural = 'Заказ:История'

    order = models.ForeignKey('order.Order', verbose_name='Заказ', on_delete=models.CASCADE)
    status = models.ForeignKey(
        'order.Status', null=True, verbose_name=BASE_STATUS_VERBOSE_NAME, on_delete=models.SET_NULL)
    total_cost = models.DecimalField(
        verbose_name='Общая стоимость', max_digits=10, decimal_places=2,
        default=0, validators=[MinValueValidator(Decimal('0'))])
    comment = models.TextField(verbose_name='Комментарий', null=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @staticmethod
    def create_or_update(order, message=''):
        from order.models.story import Story

        order.total_cost = order.get_total_cost()
        story, is_created = Story.objects.get_or_create(
            order_id=order.id, status=order.status, total_cost=order.total_cost,
            defaults={
                'comment': message,
                'status': order.status,
                'total_cost': order.total_cost
            })

        # update the current of an order item
        br = '\r' if message else ''
        if not is_created:
            story.comment += br + message
            story.status = order.status
            story.total_cost = order.total_cost
            story.save(update_fields=('comment', 'status', 'total_cost'))
