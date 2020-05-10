from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from gen.utils.url import generate_path_year_month


class BaseUserProfileModel(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = ThumbnailerImageField(upload_to=generate_path_year_month, blank=True, null=True, verbose_name='Аватар')
    patronymic = models.CharField(max_length=155, blank=True, null=True, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='День рождения', blank=True, null=True)
    phone = models.CharField(max_length=32, verbose_name='Телефон', blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True, verbose_name='Адрес')
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    id_signed_news = models.BooleanField(default=False, verbose_name='Подписан на новости')

    def __str__(self):
        return '{}'.format(self.user)

    def get_full_name(self):
        return '%s %s %s' % (self.user.last_name, self.user.first_name, self.patronymic)

    def get_short_name(self):
        short_name = '{} {}'.format(self.user.last_name, self.user.first_name)
        return short_name if self.user.first_name else None
