from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User

from gen.abstract.admin import AbstractDefaultAdmin
from gen.users.forms.user_change_form import UserChangeForm
from gen.users.strings import APP_NAME
from users.models import UserLink, UserProfile

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    verbose_name_plural = 'Профиль'
    model = UserProfile


class UserLinkInline(admin.TabularInline):
    verbose_name = 'Ссылка'
    verbose_name_plural = 'Пользовательские ссылки'
    model = UserLink
    extra = 0
    classes = ('collapse',)


@admin.register(User)
class BaseUserAdmin(DefaultUserAdmin, AbstractDefaultAdmin):
    inlines = (UserProfileInline, UserLinkInline)
    actions = AbstractDefaultAdmin.actions + ('set_fixtures', 'load_fixtures')
    form = UserChangeForm
    date_hierarchy = 'date_joined'
    readonly_fields = ('date_joined', 'last_login',)
    search_fields = ('username', 'email', 'last_name')
    list_filter = (
        'is_active', 'is_staff', 'is_superuser',
        'date_joined', 'last_login',
    )
    list_display = ('email', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    filter_horizontal = ('groups', 'user_permissions')

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseUserAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = '[не применять] Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseUserAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = '[не применять] Фикстуры: Загрузить последние'

    # TODO: [fieldsets admin]
    # fieldsets = (
    #     ('Основные данные', {
    #         'fields': (
    #             'username', 'first_name', 'last_name', 'email',
    #             ('is_active', 'is_staff', 'is_superuser')
    #         )
    #     }),
    #     ('Дополнительно', {
    #         'fields': ('groups', 'user_permissions', 'date_joined', 'last_login'),
    #         'classes': ('collapse',)
    #     }),
    #
    # )
