from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .created import AbstractCreatedModel
from .content import AbstractContentModel
from .seo import AbstractSeoModel
from gen.abstract.admin.default import BaseAdmin


class AbstractPageSeoModel(AbstractContentModel, AbstractSeoModel, AbstractCreatedModel):
    class Meta:
        abstract = True

    @classmethod
    def queryset_not_cloned(cls, flat_pk=False):
        qs = cls.objects.filter(
            is_show=True, sort__gt=0
        ).exclude(
            title__endswith=BaseAdmin.prefix_clone
        ).exclude(slug__endswith=BaseAdmin.prefix_clone)
        return qs if not flat_pk else qs.values_list('pk', flat=True)

    def get_images(self):
        raise NotImplementedError()

    def get_main_image(self):
        images = self.get_images()
        if images:
            image = images.first()
            if images.filter(image_is_main=True).exists():
                image = images.filter(image_is_main=True).first()
            # return image.image
            return image

    def set_image_title(self, obj=None):
        """
        :param obj: {object} - QuerySet object
        """
        obj = obj if obj else self

        if hasattr(obj, 'title'):
            if not self.image_title and obj.title:
                self.image_title = obj.title
        if hasattr(obj, 'get_images'):
            if not obj.get_images().filter(image_is_main=True).exists():
                self.image_is_main = True


class AbstractMPTTPageSeoModel(MPTTModel, AbstractPageSeoModel):
    class MPTTMeta:
        order_insertion_by = ('parent', 'sort')

    class Meta:
        unique_together = ('title', 'parent', 'slug')
        abstract = True

    parent = TreeForeignKey(
        'self', null=True, related_name='subitems', blank=True, db_index=True,
        verbose_name='Родительский объект', on_delete=models.SET_NULL)
