from django.db import models
from gen.abstract.models import AbstractImageModel
from gen.blog.strings import BASE_BLOG_VERBOSE_NAME, BASE_BLOG_IMAGE_VERBOSE_NAME


class BaseBlogImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_BLOG_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_BLOG_IMAGE_VERBOSE_NAME

    blog = models.ForeignKey('blog.Blog', verbose_name=BASE_BLOG_VERBOSE_NAME, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

    def save(self, *args, **kwargs):
        self.set_image_title(self.blog)
        super(BaseBlogImageModel, self).save(*args, **kwargs)

