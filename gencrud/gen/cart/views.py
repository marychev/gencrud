from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from catalog.models import ProductItem
from . cart import Cart
from gen.mixins import MainPageMixin
import json


class CartDetail(MainPageMixin, TemplateView):
    template_name = 'cart/templates/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetail, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request).get()

        return context

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        cart = Cart(self.request)

        cart_post_data = cart.prepare_data()

        if cart_post_data.get('errors', None) is None:
            cart.add(cart_post_data)
            json_response = json.dumps({'success': cart_post_data})
        else:
            json_response = json.dumps(cart_post_data)

        return HttpResponse(json_response, content_type="application/json")


def cart_remove(request, product_item_id):
    product_item = get_object_or_404(ProductItem, id=product_item_id)
    Cart(request).remove(product_item)
    return redirect('cart_detail')


def cart_clear(request):
    Cart(request).clear()
    return redirect('cart_detail')
