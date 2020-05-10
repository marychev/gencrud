from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, redirect
from gen.mixins import MainPageMixin
from gen.utils.leftbar import get_leftbar
from gen.utils.next_prev_obj import get_next_prev
from blog.forms.post_comment import CommentForm
from blog.models import Comment, Post, Blog
from django.contrib import messages


class BasePostView(MainPageMixin, TemplateView):
    template_name = "blog/templates/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BasePostView, self).get_context_data(**kwargs)

        blog = get_object_or_404(Blog, slug=kwargs['blog_slug'], is_show=True)
        post = get_object_or_404(Post, slug=kwargs['post_slug'], blog_id=blog.id, is_show=True)

        initial = {
            'obj': post,
            'request': self.request,
        }
        comment_form = CommentForm(initial=initial)

        context.update({
            'post': post,
            'next_prev': get_next_prev(Post, post),
            'comment_form': comment_form,
            'comments': Comment.objects.filter(post_id=post.id, is_show=True).select_related(),
            'leftbar': get_leftbar(Blog, post.blog),
        })

        return context

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Post, id=request.POST['post'])
        comment_form = CommentForm(request.POST, initial={'obj':obj, 'request': request})

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, ':) Сообщение отправлено!')
        else:
            messages.error(request, '(: Произошла ошибка при отправке сообщения.')
        return redirect(obj.get_absolute_url())
