from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView

from gen.mixins import MainPageMixin
from gen.page.forms.page_comment import CommentForm
from page.models.page import Page
from page.models.page_comment import PageComment


class BasePageCommentView(MainPageMixin, TemplateView):
    model = PageComment
    form_class = CommentForm
    template_name = 'page/templates/page.html'

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Page, id=request.POST.get('page'))
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, ':) Спасибо! Отзыв принят.')
        else:
            messages.error(request, '(: Произошла ошибка при отправке отзыва.')

        return redirect(obj.get_absolute_url())
