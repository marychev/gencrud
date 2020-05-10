from django.db import models

from gen.abstract.models import AbstractCommentModel
from gen.catalog.strings import (
    BASE_PRODUCT_VERBOSE_NAME, BASE_PRODUCT_COMMENT_VERBOSE_NAME, BASE_PRODUCT_COMMENT_VERBOSE_NAME_PLURAL)


class BaseProductCommentModel(AbstractCommentModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PRODUCT_COMMENT_VERBOSE_NAME
        verbose_name_plural = BASE_PRODUCT_COMMENT_VERBOSE_NAME_PLURAL

    product = models.ForeignKey(
        'catalog.Product', verbose_name=BASE_PRODUCT_VERBOSE_NAME, null=True, on_delete=models.SET_NULL)
