from django.db import models
from gen.abstract.models import AbstractImageModel
from gen.task.strings import (
    BASE_TASK_IMAGE_VERBOSE_NAME, BASE_TASK_IMAGE_VERBOSE_NAME_PLURAL, BASE_TASK_VERBOSE_NAME)


class BaseTaskImageModel(AbstractImageModel):
    class Meta:
        abstract = True
        verbose_name = BASE_TASK_IMAGE_VERBOSE_NAME
        verbose_name_plural = BASE_TASK_IMAGE_VERBOSE_NAME_PLURAL

    task = models.ForeignKey('task.Task', verbose_name=BASE_TASK_VERBOSE_NAME, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.title

    def save(self, *args, **kwargs):
        self.set_image_title(self.task)
        super(BaseTaskImageModel, self).save(*args, **kwargs)


