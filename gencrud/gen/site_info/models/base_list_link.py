from django.db import models
from gen.utils.help_text import SETTINGSTEMPLATE_TYPE_LINK_HT
from gen.site_info.strings import BASE_LIST_LINK_VERBOSE_NAME, BASE_LIST_LINK_VERBOSE_NAME_PLURAL


class BaseListLinkModel(models.Model):
    LINK = 'L'
    TAG = 'T'
    TYPE_LINK_CHOICES = (
        (LINK, 'ссылки'),
        (TAG, 'тэги (окроет в новом окне)')
    )

    class Meta:
        abstract = True
        verbose_name = BASE_LIST_LINK_VERBOSE_NAME
        verbose_name_plural = BASE_LIST_LINK_VERBOSE_NAME_PLURAL

    title = models.CharField(max_length=125, verbose_name='Заголовок', db_index=True)
    url = models.URLField(max_length=255, verbose_name='URL страницы', blank=True, null=True, db_index=True)
    sort = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', db_index=True, default=0)
    is_show = models.BooleanField(default=True, verbose_name='Показать/Скрыть')
    type_link = models.CharField(
        max_length=1, choices=TYPE_LINK_CHOICES, default=TYPE_LINK_CHOICES[0], verbose_name='Вид ссылки',
        help_text=SETTINGSTEMPLATE_TYPE_LINK_HT)

    def __str__(self):
        return self.title
