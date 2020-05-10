from django.urls import reverse
from django.db import models
from gen.abstract.models import AbstractPageSeoModel
from blog.models.post_image import PostImage
from blog.models.post_comment import Comment
from gen.blog.strings import BASE_POST_VERBOSE_NAME, BASE_POST_VERBOSE_NAME_PLURAL


class BasePostModel(AbstractPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_POST_VERBOSE_NAME
        verbose_name_plural = BASE_POST_VERBOSE_NAME_PLURAL
        ordering = ('blog', 'sort', 'is_show')

    blog = models.ForeignKey(
        'blog.Blog', verbose_name=BASE_POST_VERBOSE_NAME,
        blank=True, null=True, on_delete=models.SET_NULL)
    comment_count = models.IntegerField(blank=True, default=0, verbose_name='Кол-во коментариев')

    def get_images(self):
        return PostImage.objects.filter(post_id=self.id)

    def get_comments(self):
        qs = Comment.objects.filter(post_id=self.id)
        return qs

    def get_absolute_url(self):
        blog_slug = self.blog.slug if self.blog and self.blog.slug else 'blog'.format(self.id)
        post_slug = self.slug if self.slug else 'blog'.format(self.slug)
        kwargs = {
            'blog_slug': blog_slug,
            'post_slug': post_slug
        }
        return reverse('blog_detail', kwargs=kwargs)


