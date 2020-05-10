from django.db import models
from gen.abstract.models import AbstractImageModel
from gen.blog.strings import (
    BASE_POST_IMAGE_VERBOSE_NAME, BASE_POST_IMAGE_VERBOSE_NAME_PLURAL, BASE_POST_VERBOSE_NAME)


class BasePostImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_POST_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_POST_IMAGE_VERBOSE_NAME_PLURAL

    post = models.ForeignKey('blog.Post', verbose_name=BASE_POST_VERBOSE_NAME, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.set_image_title(self.post)
        super(BasePostImageModel, self).save(*args, **kwargs)
