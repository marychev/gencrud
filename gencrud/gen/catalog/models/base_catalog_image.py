from django.db import models
from gen.abstract.models import AbstractImageModel
from gen.catalog.strings import (BASE_CATALOG_VERBOSE_NAME, BASE_CATALOG_IMAGE_VERBOSE_NAME)


class BaseCatalogImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_CATALOG_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_CATALOG_IMAGE_VERBOSE_NAME

    catalog = models.ForeignKey('catalog.Catalog', verbose_name=BASE_CATALOG_VERBOSE_NAME, on_delete=models.CASCADE)

    def __str__(self):
        return self.catalog.title

    def save(self, *args, **kwargs):
        self.set_image_title(self.catalog)
        super().save(*args, **kwargs)
