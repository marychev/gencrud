from django.db import models
from gen.utils.translit_field import translaton_field
from gen.utils.help_text import SLUG_HT, SEO_TITLE_HT, SEO_KEYWORDS_HT, SEO_DESCRIPTION_HT, OG_LOCALE_HT, \
    SWTTINGSTEMPLATE_SCRIPTS_HT


class AbstractSeoModel(models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField(verbose_name='элемент URL', db_index=True, help_text=SLUG_HT)
    seo_title = models.CharField(
        max_length=255, verbose_name='Seo title', blank=True, null=True, help_text=SEO_TITLE_HT)
    seo_description = models.TextField(
        max_length=510, verbose_name='Seo description', blank=True, null=True, help_text=SEO_DESCRIPTION_HT)
    seo_keywords = models.TextField(
        max_length=510, verbose_name='Seo keywords', blank=True, null=True, help_text=SEO_KEYWORDS_HT)
    og_locale = models.TextField(
        max_length=510, null=True, blank=True, default='ru_RU', verbose_name='og locale', help_text=OG_LOCALE_HT)
    scripts = models.TextField(
        null=True, blank=True, verbose_name="Блок скриптов", help_text=SWTTINGSTEMPLATE_SCRIPTS_HT)

    def short_slug(self, is_save=True):
        postfix = str(self.pk) if self.pk else ''
        string = self.title[:35] if self.title else 'object-'
        short_title = '{}{}'.format(string, postfix)

        self.slug = translaton_field(short_title)

        if is_save:
            self.save(update_fields=['slug'])

    def save(self, *args, **kwargs):
        from gen.utils.auto_seo import AutoSeo
        AutoSeo(page=self, title=self.title).default()

        max_length = 50
        if not self.slug or len(self.slug) > max_length:
            self.short_slug(False)

        super(AbstractSeoModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if not self.slug:
            self.short_slug()
