from django.db import models

from gen.abstract.models import AbstractImageModel
from gen.page.strings import (
    BASE_PAGE_VERBOSE_NAME, BASE_PAGE_IMAGE_VERBOSE_NAME, BASE_PAGE_IMAGE_VERBOSE_NAME_PLURAL)


class BasePageImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PAGE_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_PAGE_IMAGE_VERBOSE_NAME_PLURAL

    page = models.ForeignKey('page.Page', verbose_name=BASE_PAGE_VERBOSE_NAME, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.set_image_title(self.page)
        super().save(*args, **kwargs)
