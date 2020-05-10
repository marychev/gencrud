from django.db import models
from django.contrib.auth.models import User


class BaseUserLinkModel(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    anchor = models.CharField(max_length=100, verbose_name='Название ссылки / текст привязки', blank=True, null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.anchor
