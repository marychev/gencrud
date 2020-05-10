from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from gen.utils.help_text import SORT_HT


class AbstractTitleModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        max_length=255, db_index=True, verbose_name='Заголовок',
        default='заголовок объекта')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title


class AbstractContentModel(AbstractTitleModel):
    class Meta:
        ordering = 'sort'
        abstract = True

    html = RichTextUploadingField(verbose_name='HTML/Текст', blank=True, null=True)
    is_show = models.BooleanField(default=True, verbose_name='Отображать')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Автор', blank=True, null=True, on_delete=models.SET_NULL)
    sort = models.SmallIntegerField(default=1000, verbose_name='Сортировка', help_text=SORT_HT)

    tags = models.ManyToManyField('site_info.Tag', verbose_name='Тэги', blank=True)
    is_allow_comments = models.BooleanField(default=False, verbose_name='разрешить комментарии')
