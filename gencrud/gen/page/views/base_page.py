from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from blog.models import Blog
from gen.mixins import MainPageMixin
from gen.page.forms.page_comment import CommentForm
from gen.utils.leftbar import get_leftbar
from page.models.page import Page


class BasePageView(MainPageMixin, TemplateView):
    template_name = 'page/templates/page.html'

    def get_context_data(self, **kwargs):
        context = super(BasePageView, self).get_context_data(**kwargs)

        context['object'] = get_object_or_404(Page, slug=context['slug'], is_show=True)
        initial = {
            'obj': context['object'],
            'request': self.request,
        }
        comment_form = CommentForm(initial=initial)
        context['comment_form'] = comment_form
        context['leftbar'] = get_leftbar(Blog, Blog.objects.first())

        return context
