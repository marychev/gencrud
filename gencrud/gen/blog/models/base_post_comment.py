from django.db import models
from django.db.models.signals import post_save
from gen.abstract.models import AbstractCommentModel
from gen.blog.signals import save_comment
from gen.blog.strings import (
    BASE_POST_VERBOSE_NAME, BASE_POST_COMMENT_VERBOSE_NAME, BASE_POST_COMMENT_VERBOSE_NAME_PLURAL)


class BasePostComment(AbstractCommentModel):
    class Meta:
        abstract = True
        verbose_name = BASE_POST_COMMENT_VERBOSE_NAME
        verbose_name_plural = BASE_POST_COMMENT_VERBOSE_NAME_PLURAL

    post = models.ForeignKey('blog.Post', verbose_name=BASE_POST_VERBOSE_NAME, null=True, on_delete=models.SET_NULL)


post_save.connect(save_comment, sender=BasePostComment)
