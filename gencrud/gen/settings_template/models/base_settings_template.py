from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sites.models import Site
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from gen.home.strings import BASE_HOME_VERBOSE_NAME
from gen.settings_template.strings import (BASE_SETTINGS_TEMPLATE_VERBOSE_NAME, BASE_FOOTER_VERBOSE_NAME)
from gen.utils.help_text import (
    ROBOTS_TXT_HT, SWTTINGSTEMPLATE_TITLE_HT, SWTTINGSTEMPLATE_PHONE_HT,
    SWTTINGSTEMPLATE_IS_INCLUDED_HT, SWTTINGSTEMPLATE_LOGO_HT, SWTTINGSTEMPLATE_SCRIPTS_HT,
    SWTTINGSTEMPLATE_META_HT, TERMS_OF_USE)
from gen.utils.url import generate_path_year_month
from home.models import Home


class BaseSettingsTemplateModel(models.Model):
    class Meta:
        abstract = True
        verbose_name = BASE_SETTINGS_TEMPLATE_VERBOSE_NAME
        verbose_name_plural = BASE_SETTINGS_TEMPLATE_VERBOSE_NAME

    title = models.CharField(
        max_length=125, verbose_name='Заголовок', unique=True,
        help_text=SWTTINGSTEMPLATE_TITLE_HT, default='Основной шаблон')
    is_included = models.BooleanField(
        default=False, verbose_name='Включена',
        help_text=SWTTINGSTEMPLATE_IS_INCLUDED_HT)
    site = models.OneToOneField(Site, verbose_name='Сайт/Домен', blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(verbose_name='Email проекта', blank=True)
    phone = models.CharField(
        max_length=30, blank=True, null=True, verbose_name='Номер телефона',
        help_text=SWTTINGSTEMPLATE_PHONE_HT, unique=True)
    address = models.CharField(max_length=255, default="Адрес", blank=True, null=True, verbose_name="Адрес")
    logo = ThumbnailerImageField(
        upload_to=generate_path_year_month, blank=True, null=True,
        verbose_name='Логотип', help_text=SWTTINGSTEMPLATE_LOGO_HT)

    home = models.ForeignKey(
        Home, verbose_name=BASE_HOME_VERBOSE_NAME,
        blank=True, null=True, on_delete=models.SET_NULL)
    footer = models.ForeignKey(
        'settings_template.Footer', verbose_name=BASE_FOOTER_VERBOSE_NAME,
        blank=True, null=True, on_delete=models.SET_NULL)

    robots_txt = models.TextField(
        null=True, blank=True, verbose_name="Содержимое robots.txt",
        default=ROBOTS_TXT_HT, help_text=ROBOTS_TXT_HT)

    meta = models.TextField(
        null=True, blank=True, verbose_name="Блок Мета-тегов", help_text=SWTTINGSTEMPLATE_META_HT)

    scripts = models.TextField(
        null=True, blank=True, verbose_name="Блок скриптов", help_text=SWTTINGSTEMPLATE_SCRIPTS_HT)

    terms_of_use = RichTextUploadingField(
        null=True, blank=True, verbose_name="Пользовотельское соглашение",
        help_text=TERMS_OF_USE)

    def __str__(self):
        return self.title

    def get_main_image(self):
        return self.logo if self.logo else None

