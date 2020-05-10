from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from gen.mixins import MainPageMixin
from gen.utils.pagination import get_pagination
from gen.utils.leftbar import get_leftbar
from gen.utils.sort import sort_by_params

from blog.models import Blog, Post


class BaseBlogView(MainPageMixin, TemplateView):
    template_name = 'blog/templates/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(BaseBlogView, self).get_context_data(**kwargs)

        context['object'] = get_object_or_404(Blog, slug=context['slug'], is_show=True)
        context['leftbar'] = get_leftbar(Blog, context['object'])
        blog_id = context['leftbar']['root_obj'].id
        context['current_mainmenu'] = context['mainmenu'].filter(
            blog_id=blog_id, is_show=True,
        ).first()
        context['objects'] = Post.objects.filter(blog_id=context['object'].id, is_show=True)
        context['objects'] = sort_by_params(self.request, context['objects'])
        context['objects'] = get_pagination(self.request, context['objects'])

        return context

