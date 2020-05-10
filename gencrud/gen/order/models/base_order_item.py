from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from catalog.models import ProductItem
from order.models.story import Story
from gen.order.strings import BASE_ORDER_ITEM_VERBOSE_NAME, BASE_ORDER_ITEM_VERBOSE_NAME_PLURAL

MSG_PRODUCT_PRICE_CHANGE = '[*]Цена изменена. Товар:`{}` {} x {} = {} p'
MSG_PRODUCT_QTY_CHANGE = '[*]Кол-во изменено. Товар:`{}` {} x {} = {} p'
MSG_PRODUCT_ADD = '[+]Добавлен товар `{}` {} x {} = {} p'
MSG_PRODUCT_DELETE = '[-]Удален товар `{}` {} x {} = {} p'


class BaseOrderItemModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_ORDER_ITEM_VERBOSE_NAME
        verbose_name_plural = BASE_ORDER_ITEM_VERBOSE_NAME_PLURAL

    order = models.ForeignKey('order.Order', verbose_name='Заказ', on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, verbose_name='Вариант товара', on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во', default=1)

    def __str__(self):
        return '{}'.format(self.pk)

    # todo: fix with cart methods
    def get_cost(self):
        return Decimal(self.price) * int(self.quantity)

    def save(self, *args, **kwargs):
        from order.models.order_item import OrderItem

        try:
            old_obj = OrderItem.objects.get(id=self.id)
        except OrderItem.DoesNotExist:
            old_obj = self

        old_qty = old_obj.quantity
        old_count_items = self.order.orderitem_set.count()

        super(BaseOrderItemModel, self).save(*args, **kwargs)

        current_count_items = self.order.orderitem_set.count()
        current_qty = self.quantity

        # change product price
        if old_obj.price != self.price:
            message = MSG_PRODUCT_PRICE_CHANGE.format(
                self.product_item, self.price, self.quantity, self.get_cost())
            Story.create_or_update(self.order, message)

        # change count of the product item
        if current_qty != old_qty:
            message = MSG_PRODUCT_QTY_CHANGE.format(
                self.product_item, self.price, self.quantity, self.get_cost())
            Story.create_or_update(self.order, message)

        # add a new product item
        if old_count_items < current_count_items:
            message = MSG_PRODUCT_ADD.format(
                self.product_item, self.price, self.quantity, self.get_cost())

            Story.create_or_update(self.order, message)

        # a new save the order, because data was changed
        self.order.save()

    def delete(self, *args, **kwargs):
        old_count_items = self.order.orderitem_set.count()

        super(BaseOrderItemModel, self).delete(*args, **kwargs)

        current_count_items = self.order.orderitem_set.count()

        # delete a product item
        if old_count_items > current_count_items:
            message = MSG_PRODUCT_DELETE.format(
                self.product_item, self.price, self.quantity, self.get_cost())
            Story.create_or_update(self.order, message)

        # a new save the order, because data was changed
        self.order.save()


