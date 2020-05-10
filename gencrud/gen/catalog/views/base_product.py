import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from catalog.models import Catalog, Product, ProductItem, ProductComment
from gen.cart.cart import Cart
from gen.cart.forms import CartAddProductForm
from gen.catalog.forms.product_comment import CommentForm
from gen.mixins import MainPageMixin
from gen.utils.leftbar import get_leftbar
from gen.utils.next_prev_obj import get_next_prev


class BaseProductDetailView(MainPageMixin, TemplateView):
    template_name = Product.DEFAULT_LAYOUT

    def __try_fix_MultipleObjectsReturned(self, kwargs):
        from gen.utils.todo import create_bug_issue

        title = 'ERROR. Product MultipleObjectsReturned. "slug": {}'.format(kwargs['product'])
        create_bug_issue(title)

        product_exists = Product.objects.filter(slug=kwargs['product'], is_show=True)
        [p.short_slug() for p in product_exists]

    def get_context_data(self, **kwargs):
        context = super(BaseProductDetailView, self).get_context_data(**kwargs)

        try:
            context['product'] = get_object_or_404(Product, slug=kwargs['product'], is_show=True)

            self.template_name = context['product'].layout or Product.DEFAULT_LAYOUT
        except Product.MultipleObjectsReturned:
            self.__try_fix_MultipleObjectsReturned(kwargs)
            raise Http404('HOW FIX: Return into catalog and click on this product again!')

        initial = {
            'obj': context['product'],
            'request': self.request,
        }
        comment_form = CommentForm(initial=initial)
        context['comment_form'] = comment_form
        context['comments'] = ProductComment.objects.filter(
            is_show=True, product_id=context['product'].id)
        context['catalog'] = get_object_or_404(Catalog, slug=kwargs['catalog'])
        context['cart_product_form'] = CartAddProductForm()
        context['next_prev'] = get_next_prev(Product, context['product'])
        context['leftbar'] = get_leftbar(Catalog, context['catalog'])

        return context

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # todo: check and remove
        obj = ProductItem.objects.get(id=request.POST['product_id'])
        response_data = {
            'product_id': obj.id,
            'name': obj.name,
            'articul': obj.articul,
            'quantity': int(request.POST.get('quantity', 0)),
            'price': float(obj.price)
        }

        cart = Cart(request).get()
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=obj, quantity=cd['quantity'], is_update_qty=cd['is_update'])

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    @staticmethod
    def get_context_for_catalog(context):
        """        Todo: need to fix        """
        context['template_name'] = 'product_detail.html'
        context['product'] = get_object_or_404(Product, slug=context['slug'])

        initial = {
            'obj': context['product'],
            'request': context['request'],
        }
        comment_form = CommentForm(initial=initial)
        context['comment_form'] = comment_form
        context['comments'] = ProductComment.objects.filter(is_show=True, product_id=context['product'].id)
        context['catalog'] = context['product'].catalog.first()
        context['cart_product_form'] = CartAddProductForm()
        context['next_prev'] = get_next_prev(Product, context['product'])
        context['leftbar'] = get_leftbar(Catalog, context['catalog'])

        return context

