from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from gen.utils.thumbnail import resize
from gen.abstract.models import AbstractImageModel
from gen.utils.help_text import SOCIAL_NETWORK_HTML_LINK_HT
from gen.utils.url import generate_path_year_month
from gen.site_info.strings import BASE_SOCIAL_NETWORK_VERBOSE_NAME, BASE_SOCIAL_NETWORK_VERBOSE_NAME_PLURAL


class BaseSocialNetworkModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_SOCIAL_NETWORK_VERBOSE_NAME
        verbose_name_plural = BASE_SOCIAL_NETWORK_VERBOSE_NAME_PLURAL

    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    image = ThumbnailerImageField(upload_to=generate_path_year_month, blank=True, null=True, verbose_name='Иконка')
    html_link = models.CharField(
        verbose_name='НТМЛ-ссылка', max_length=512, unique=True, blank=True, null=True,
        help_text=SOCIAL_NETWORK_HTML_LINK_HT)
    url = models.URLField(verbose_name='URL страницы', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_html_links(self):
        from site_info.models.social_network import SocialNetwork
        return SocialNetwork.objects.filter(image__isnull=True, html_link__isnull=False).values('html_link',)

    def save(self, *args, **kwargs):
        super(BaseSocialNetworkModel, self).save(*args, **kwargs)

        # --resizing image
        if self.image and (self.image.width > 200 or self.image.height > 200):
            resize(self.image.path, (200, 200), True)
