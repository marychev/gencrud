from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from gen.catalog.forms.product_comment import CommentForm

from catalog.models import Product, ProductComment
from gen.mixins import MainPageMixin


class BaseProductCommentView(MainPageMixin, TemplateView):
    form_class = CommentForm
    model = ProductComment
    template_name = 'product/templates/product_detail.html'

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Product, id=request.POST.get('product'))
        review_form = CommentForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, ':) Спасибо! Комментарий оставлен.')
        else:
            messages.error(request, '(: Произошла ошибка при отправке отзыва.')
        return redirect(obj.get_absolute_url())
