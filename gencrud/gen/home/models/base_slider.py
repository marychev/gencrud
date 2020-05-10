from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.html import format_html
from gen.utils.help_text import URL_HT, SORT_HT
from gen.utils.url import generate_path_year_month
from gen.abstract.models import AbstractTitleModel
from gen.home.strings import BASE_HOME_SLIDER_HOME_VERBOSE_NAME, BASE_HOME_SLIDER_HOME_VERBOSE_NAME_PLURAL


class BaseSliderHomeModel(AbstractTitleModel):
    class Meta:
        abstract = True
        ordering = ('sort',)
        verbose_name = BASE_HOME_SLIDER_HOME_VERBOSE_NAME
        verbose_name_plural = BASE_HOME_SLIDER_HOME_VERBOSE_NAME_PLURAL

    image = ThumbnailerImageField(upload_to=generate_path_year_month, blank=True, null=True, verbose_name='Изображение')
    url = models.URLField('Полный путь к веб-странице', null=True, blank=True, help_text=URL_HT)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True, help_text=SORT_HT, default=1000)

    def __str__(self):
        return self.title

    def html_description(self):
        return format_html(self.description)

    def get_main_image(self):
        from home.models.slider import SliderHome
        return SliderHome.objects.all().first()

# [!] NOT DELETE ---
# -------------------

# image = models.ImageField(upload_to='slider/', verbose_name='Изображение')

# def save(self, *args, **kwargs):
#     from sorl.thumbnail import ImageField, delete, get_thumbnail
#     from gen.utils.thumbnail import resize, get_thumb
#     super(SliderHome, self).save(*args, **kwargs)
#     if self.image and (self.image.width > 1400 or self.image.height > 1000):
#         resize(self.image.path, (1400, 1000))
