from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from gen.utils.url import generate_path_year_month
from gen.utils.help_text import SORT_HT, IA_CODE_HT, URL_HT
from gen.site_info.strings import BASE_INCLUDE_AREA_VERBOSE_NAME, BASE_INCLUDE_AREA_VERBOSE_NAME_PLURAL


class BaseIncludeAreaModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_INCLUDE_AREA_VERBOSE_NAME
        verbose_name_plural = BASE_INCLUDE_AREA_VERBOSE_NAME_PLURAL
        ordering = ('sort', 'code')
        unique_together = ('title', 'code')

    ADVANTAGES = 'advantages'
    BRANDS = 'brands'
    COUNTER = 'counter'
    CODE_CHOICES = (
        (ADVANTAGES, 'Наши преимущества'),
        (BRANDS, 'Брэнды'),
        (COUNTER, 'Счетчик'),
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    is_show = models.BooleanField(default=True, verbose_name="Отображать")
    image = ThumbnailerImageField(upload_to=generate_path_year_month, blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    code = models.CharField(
        max_length=20, choices=CODE_CHOICES, default=ADVANTAGES, verbose_name="Код", help_text=IA_CODE_HT)
    sort = models.PositiveSmallIntegerField(default=1000, verbose_name='Сортировка', help_text=SORT_HT)
    url = models.URLField('Полный путь к веб-странице', null=True, blank=True, help_text=URL_HT)

    def __str__(self):
        return self.title

    def get_html(self):
        # from django.template import Template, Context
        # template = Template('advantages.html')
        # c = Context({'include_area': self})
        # return template.render(c)

        from django.template.loader import render_to_string
        from site_info.models.include_area import IncludeArea

        return render_to_string('{}.html'.format(self.code), {
            'include_area': IncludeArea.objects.filter(code=self.code)
        })

    def get_main_image(self):
        return self.image if self.image else None

