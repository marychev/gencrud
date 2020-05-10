from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from blog.models import Blog
from catalog.models import Catalog
from gen.settings_template.strings import BASE_MENU_VERBOSE_NAME, BASE_MENU_VERBOSE_NAME_PLURAL
from gen.blog.strings import BASE_BLOG_VERBOSE_NAME
from gen.page.strings import BASE_PAGE_VERBOSE_NAME
from gen.utils.help_text import SORT_HT
from page.models import Page
from gen.abstract.admin.default import BaseAdmin
from gen.settings_template.models.menu_limit_choices import (
    menu_limit_choices_to_blog, menu_limit_choices_to_catalog,
    menu_limit_choices_to_parent, menu_limit_choices_to_page
)


class BaseMenuModel(MPTTModel):
    class Meta:
        abstract = True
        verbose_name = BASE_MENU_VERBOSE_NAME
        verbose_name_plural = BASE_MENU_VERBOSE_NAME_PLURAL
        unique_together = ('name', 'parent', 'is_show')

    class MPTTMeta:
        order_insertion_by = ('parent', 'sort')

    name = models.CharField(max_length=80, null=True, verbose_name='название', db_index=True)
    parent = TreeForeignKey(
        'self', verbose_name='родительская категория',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='child',
        limit_choices_to=menu_limit_choices_to_parent)
    is_show = models.BooleanField(default=True, verbose_name='Отображать')
    catalog = models.ForeignKey(
        Catalog, blank=True, null=True, verbose_name='каталог', on_delete=models.SET_NULL,
        limit_choices_to=menu_limit_choices_to_catalog,
    )
    blog = models.ForeignKey(
        Blog,  blank=True, null=True, verbose_name=BASE_BLOG_VERBOSE_NAME,
        on_delete=models.SET_NULL,
        limit_choices_to=menu_limit_choices_to_blog
    )
    page = models.ForeignKey(
        Page, blank=True, null=True, verbose_name=BASE_PAGE_VERBOSE_NAME,
        on_delete=models.SET_NULL,
        limit_choices_to=menu_limit_choices_to_page
    )
    sort = models.SmallIntegerField(default=1000, verbose_name='Сортировка', help_text=SORT_HT)

    def __str__(self):
        return self.name

    @classmethod
    def get_absolute_url_item(cls, item):
        if item.catalog:
            return item.catalog.get_absolute_url
        elif item.blog:
            return item.blog.get_absolute_url
        elif item.page:
            return item.page.get_absolute_url

    def get_url(self):
        slug = self.get_absolute_url_item(self)

        if self.get_children().exists():
            slug = [self.get_absolute_url_item(item) for item in self.get_children()]

        return slug or '/'

    def save(self, *args, **kwargs):
        super(BaseMenuModel, self).save(*args, **kwargs)
        self.model.objects.rebuild()

    @classmethod
    def queryset_not_cloned(cls, flat_pk=False):
        qs = cls.objects.filter(is_show=True, sort__gt=0).exclude(
            name__endswith=BaseAdmin.prefix_clone)
        return qs if not flat_pk else qs.values_list('pk', flat=True)
