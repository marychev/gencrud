from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from gen.mixins import MainPageMixin
from gen.cart.cart import Cart
from catalog.models import ProductItem
from order.models.order_item import OrderItem
from gen.order.forms.order_create import OrderCreateForm
from gen.order.strings import APP_NAME


@method_decorator(login_required, name='dispatch')
class BaseOrderCreateModel(MainPageMixin, TemplateView):
    template_name = '{}/templates/create.html'.format(APP_NAME)

    def get_context_data(self, **kwargs):
        context = super(BaseOrderCreateModel, self).get_context_data(**kwargs)

        context['cart'] = Cart(self.request).get()
        context['form'] = OrderCreateForm(
            initial={'cart': context['cart'], 'user': context['request'].user})
        context['breadcrumbs'] = [
            {'title': 'Корзина', 'url': '/cart/'},
            {'title': 'Оформление заказа', 'url': '/{}/create/'.format(APP_NAME)}
        ]
        context['order'] = None
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        _cart = Cart(request)

        form = OrderCreateForm(
            request.POST, initial={
                'cart': _cart,
                'user': context['request'].user
            })

        if form.is_valid():
            context['order'] = form.save()

            for item in _cart.get():
                for pi in item['productItems']:
                    product_item = ProductItem.objects.get(pk=int(pi['id']))
                    oi = OrderItem(
                        order=context['order'], product_item=product_item,
                        price=pi['price'], quantity=pi['count'])
                    oi.save()

            _cart.clear()

            return redirect('/{}/'.format(APP_NAME) + str(context['order'].pk) + '/created/')
        return render(request, self.template_name, context=context)
