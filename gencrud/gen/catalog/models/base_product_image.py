from django.db import models
from gen.abstract.models import AbstractImageModel
from gen.catalog.strings import BASE_PRODUCT_VERBOSE_NAME, BASE_PRODUCT_IMAGE_VERBOSE_NAME


class BaseProductImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PRODUCT_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_PRODUCT_IMAGE_VERBOSE_NAME

    product = models.ForeignKey(
        'catalog.Product', verbose_name=BASE_PRODUCT_VERBOSE_NAME, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.set_image_title(self.product)
        super(BaseProductImageModel, self).save(*args, **kwargs)

