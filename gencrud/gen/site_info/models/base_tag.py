from django.db import models
from gen.site_info.strings import BASE_TAG_VERBOSE_NAME, BASE_TAG_VERBOSE_NAME_PLURAL


class BaseTagModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('title',)
        verbose_name = BASE_TAG_VERBOSE_NAME
        verbose_name_plural = BASE_TAG_VERBOSE_NAME_PLURAL

    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title
