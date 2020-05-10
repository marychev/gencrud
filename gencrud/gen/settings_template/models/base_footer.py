from django.db import models

from blog.models.blog import Blog
from catalog.models import Catalog
from gen.blog.strings import BASE_BLOG_VERBOSE_NAME_PLURAL
from gen.catalog.strings import BASE_CATALOG_VERBOSE_NAME_PLURAL
from gen.page.strings import BASE_PAGE_VERBOSE_NAME_PLURAL
from gen.settings_template.strings import BASE_FOOTER_VERBOSE_NAME
from page.models.page import Page
from site_info.models import ListLink, TextInfo


class BaseFooterModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_FOOTER_VERBOSE_NAME
        verbose_name_plural = BASE_FOOTER_VERBOSE_NAME

    title = models.CharField(
        max_length=125, verbose_name='Заголовок', unique=True, default='Нижний футер')
    list_link = models.ManyToManyField(ListLink, verbose_name='Быстрые ссылки', blank=True)
    text_info = models.ForeignKey(
        TextInfo, verbose_name='Текстовая информация', blank=True, null=True, on_delete=models.CASCADE)
    catalog = models.ManyToManyField(
        Catalog, verbose_name=BASE_CATALOG_VERBOSE_NAME_PLURAL,
        limit_choices_to={'is_show': True}, blank=True)
    page = models.ManyToManyField(
        Page, verbose_name=BASE_PAGE_VERBOSE_NAME_PLURAL,
        limit_choices_to={'is_show': True}, blank=True)
    blogs = models.ManyToManyField(
        Blog, verbose_name=BASE_BLOG_VERBOSE_NAME_PLURAL,
        limit_choices_to={'is_show': True}, blank=True)
    is_show = models.BooleanField(default=True, verbose_name='Отображать')

    def __str__(self):
        return self.title

    def get_list_link(self):
        return self.list_link.filter(is_show=True)


