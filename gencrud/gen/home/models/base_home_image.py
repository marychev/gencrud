from django.db import models
from gen.home.strings import (
    BASE_HOME_VERBOSE_NAME, BASE_HOME_IMAGE_VERBOSE_NAME, BASE_HOME_IMAGE_VERBOSE_NAME_PLURAL)
from gen.abstract.models import AbstractImageModel


class BaseHomeImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_HOME_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_HOME_IMAGE_VERBOSE_NAME_PLURAL

    home = models.ForeignKey('home.Home', verbose_name=BASE_HOME_VERBOSE_NAME, on_delete=models.CASCADE)

    def __str__(self):
        return self.home.title

    def save(self, *args, **kwargs):
        self.set_image_title(self.home)
        super().save(*args, **kwargs)
