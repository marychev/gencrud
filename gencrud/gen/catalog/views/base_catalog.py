import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from catalog.models import Catalog, Product, ProductItem
from gen.mixins import MainPageMixin
from gen.utils.leftbar import get_leftbar
from gen.utils.pagination import get_pagination
from gen.utils.sort import (sort_by_params, get_filter, filter_by_param)


class BaseCatalogView(MainPageMixin, TemplateView):
    template_name = 'catalog/templates/catalog.html'

    def get_context_data(self, **kwargs):
        context = super(BaseCatalogView, self).get_context_data(**kwargs)

        context['object'] = get_object_or_404(Catalog, slug=context['slug'], is_show=True)
        context['leftbar'] = get_leftbar(Catalog, context['object'])

        catalog_id = context['leftbar']['root_obj'].id
        context['current_mainmenu'] = context['mainmenu'].filter(catalog_id=catalog_id).first()

        context['objects'] = Product.objects.filter(catalogs=context['object'], is_show=True).order_by('-id')
        context['filter'] = get_filter(self.request, context['objects'])
        context['objects'] = filter_by_param(self.request, context['objects'])
        context['objects'] = sort_by_params(self.request, context['objects'])
        context['objects'] = get_pagination(self.request, context['objects'])

        return context

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        obj = ProductItem.objects.get(id=request.POST['product_id'])

        from catalog.views import ProductDetail
        product_detail = ProductDetail()
        product_detail.post(request)

        response_data = {
            'product_id': obj.id,
            'name': obj.name,
            'articul': obj.articul,
            'quantity': int(request.POST.get('quantity', 0)),
            'price': float(obj.price)
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")



