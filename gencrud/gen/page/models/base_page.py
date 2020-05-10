from django.db import models
from django.urls import reverse

from gen.abstract.models import AbstractPageSeoModel
from gen.page.strings import (BASE_PAGE_VERBOSE_NAME, BASE_PAGE_VERBOSE_NAME_PLURAL)
from page.models.page_image import PageImage
from page.models.page_comment import PageComment


class BasePageModel(AbstractPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_PAGE_VERBOSE_NAME
        verbose_name_plural = BASE_PAGE_VERBOSE_NAME_PLURAL

    video = models.FileField(upload_to='video/', null=True, blank=True, verbose_name='Видео')

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])

    def get_comments(self):
        qs = PageComment.objects.filter(page_id=self.pk)
        return qs

    def get_images(self):
        return PageImage.objects.filter(page_id=self.pk)
