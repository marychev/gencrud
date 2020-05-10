from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from gen.utils.url import generate_path_year_month


class AbstractImageModel(models.Model):
    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
        abstract = True

    image = ThumbnailerImageField(upload_to=generate_path_year_month, blank=True, null=True, verbose_name='Изображение')
    image_title = models.CharField(max_length=255, verbose_name='Название фото', blank=True, null=True)
    image_is_main = models.BooleanField(
        default=False, verbose_name='Главное', help_text='Главным может быть только одно фото')
    image_description = models.TextField(verbose_name='Краткое описание фото', blank=True, null=True)

    def set_image_title(self, obj):
        """
        :param obj: {object} - QuerySet object
        """
        if hasattr(obj, 'title'):
            if not self.image_title and obj.title:
                self.image_title = obj.title
        if hasattr(obj, 'get_images'):
            if obj.get_images().exists() and not obj.get_images().filter(image_is_main=True).exists():
                self.image_is_main = True
