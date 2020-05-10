from django.db import models
from gen.abstract.models import AbstractPageSeoModel
from blog.models import Blog
from catalog.models import Catalog
from home.models.home_image import HomeImage
from gen.home.strings import BASE_HOME_VERBOSE_NAME, BASE_HOME_VERBOSE_NAME_PLURAL


class BaseHomeModel(AbstractPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_HOME_VERBOSE_NAME
        verbose_name_plural = BASE_HOME_VERBOSE_NAME_PLURAL

    blog = models.ForeignKey(
        Blog, verbose_name='Блог', blank=True, null=True,
        help_text='Например, создать блог ПОСЛЕДНЕИ НОВОСТИ и закрепить его на главную страницу.',
        on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/', null=True, blank=True, verbose_name='Видео')
    catalogs = models.ManyToManyField(
        Catalog, blank=True, verbose_name='каталоги',
        limit_choices_to={'is_show': True})

    def get_images(self):
        return HomeImage.objects.filter(home_id=self.pk)



