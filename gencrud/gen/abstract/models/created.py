from django.db import models


class AbstractCreatedModel(models.Model):
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обнавлен', auto_now=True)

    class Meta:
        abstract = True
