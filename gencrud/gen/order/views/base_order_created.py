from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from gen.mixins import MainPageMixin


class BaseOrderCreatedView(MainPageMixin, TemplateView):
    template_name = 'order/templates/created.html'

    def get_context_data(self, **kwargs):
        context = super(BaseOrderCreatedView, self).get_context_data(**kwargs)

        context['breadcrumbs'] = [
            {'title': 'Корзина', 'url': '/cart/'},
            {'title': 'Заказ {}'.format(context['pk']),
                'url': 'users/{}/order'.format(context['pk'])}
        ]
        return context


