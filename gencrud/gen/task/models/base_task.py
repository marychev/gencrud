from django.urls import reverse
from gen.abstract.models import AbstractMPTTPageSeoModel
from task.models.task_image import TaskImage
from gen.task.strings import BASE_TASK_VERBOSE_NAME, BASE_TASK_VERBOSE_NAME_PLURAL
from gen.task.strings import NAME_APP as TASK_NAME_APP


class BaseTaskModel(AbstractMPTTPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_TASK_VERBOSE_NAME
        verbose_name_plural = BASE_TASK_VERBOSE_NAME_PLURAL
        unique_together = ('title', 'parent', 'slug')

    class MPTTMeta:
        order_insertion_by = ('parent', 'sort')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        super().get_absolute_url()

        kwargs = {
            'slug': self.slug,
            # 'year': '%04d' % self.created.year,
            # 'month': '%02d' % self.created.month,
            # 'day': '%02d' % self.created.day,
        }
        return reverse(TASK_NAME_APP, kwargs=kwargs)

    def get_images(self):
        return TaskImage.objects.filter(task_id=self.pk)


