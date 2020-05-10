from django.urls import reverse
from gen.abstract.models import AbstractMPTTPageSeoModel
from blog.models.blog_image import BlogImage
from gen.blog.strings import BASE_BLOG_VERBOSE_NAME, BASE_BLOG_VERBOSE_NAME_PLURAL, APP_NAME


class BaseBlogModel(AbstractMPTTPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_BLOG_VERBOSE_NAME
        verbose_name_plural = BASE_BLOG_VERBOSE_NAME_PLURAL

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse(APP_NAME, kwargs=kwargs)

    def get_images(self):
        return BlogImage.objects.filter(blog_id=self.pk)



