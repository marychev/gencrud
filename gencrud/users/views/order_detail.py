from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from gen.mixins import MainPageMixin
from order.models.order import Order


class OrderDetail(MainPageMixin, TemplateView):
    """
    Детальная информация о заказе
    """
    template_name = 'users/templates/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=context['pk'])
        context['breadcrumbs'] = [
            {'title': 'Все заказы', 'url': '/users/orders/'},
            {'title': 'Заказ {}'.format(context['pk']),
                'url': '/users/{}/order/'.format(context['pk'])}
        ]
        return context

