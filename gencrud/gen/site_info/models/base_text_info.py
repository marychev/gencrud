from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from gen.site_info.strings import BASE_TEXT_INFO_VERBOSE_NAME


class BaseTextInfoModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_TEXT_INFO_VERBOSE_NAME
        verbose_name_plural = BASE_TEXT_INFO_VERBOSE_NAME

    title = models.CharField(max_length=125, verbose_name='Заголовок', unique=True)
    html = RichTextUploadingField(verbose_name='Текст/HTML')

    def __str__(self):
        return self.title

