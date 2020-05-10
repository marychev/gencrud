from django.db import models

from gen.abstract.models import AbstractCommentModel
from gen.page.strings import (BASE_PAGE_COMMENT_VERBOSE_NAME, BASE_PAGE_COMMENT_VERBOSE_NAME_PLURAL)
from gen.page.strings import BASE_PAGE_VERBOSE_NAME


class BasePageComment(AbstractCommentModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PAGE_COMMENT_VERBOSE_NAME
        verbose_name_plural = BASE_PAGE_COMMENT_VERBOSE_NAME_PLURAL

    page = models.ForeignKey(
        'page.Page', verbose_name=BASE_PAGE_VERBOSE_NAME, null=True, on_delete=models.SET_NULL)
