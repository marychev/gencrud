from django.db import models

from gen.catalog.models.base_product_comment import BaseProductCommentModel
from gen.catalog.strings import BASE_PRODUCT_COMMENT_VERBOSE_NAME


class ProductComment(BaseProductCommentModel):
    product = models.ForeignKey(
        'catalog.Product', verbose_name=BASE_PRODUCT_COMMENT_VERBOSE_NAME, null=True, on_delete=models.SET_NULL)
