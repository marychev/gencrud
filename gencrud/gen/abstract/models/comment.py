from django.db import models
from django.conf import settings
from gen.abstract.models import AbstractCreatedModel


class AbstractCommentModel(AbstractCreatedModel):
    class Meta:
        abstract = True
        ordering = ('created',)

    text = models.TextField(verbose_name='Комментарий')
    ip_address = models.GenericIPAddressField(default='0.0.0.0', verbose_name='IP address', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='Пользователь', on_delete=models.CASCADE)
    username = models.CharField(max_length=125, default='anonymous', blank=True, null=True, verbose_name='Имя пользователя')
    email = models.EmailField(blank=True, verbose_name='Email')
    is_show = models.BooleanField(default=False, verbose_name='Отображать')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if self.user:
            self.username = self.user.username if self.user.username else self.username
            self.email = self.user.email if self.user.email else self.email
        super().save(*args, **kwargs)

