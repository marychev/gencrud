import os
import sys
from django.contrib import admin, messages
from django.utils.html import mark_safe
from django.core.management import call_command, CommandError
from mptt.admin import MPTTModelAdmin
from gen.abstract.mixins.clone import CloneObjectMixin


def dir_name_object(obj):
    f = sys.modules[obj.__module__].__file__
    return os.path.splitext(os.path.basename(f))[0]


class BaseAdmin(CloneObjectMixin):
    empty_value_display = '-'
    save_on_top = True

    def get_html(self, obj):
        return mark_safe('{}'.format(obj.html))  # [:300])
    get_html.short_description = 'HTML'

    def clone_object(self, request, queryset):
        self.clone_queryset(request, queryset)
    clone_object.short_description = CloneObjectMixin.short_description

    def set_fixtures(self, request, queryset, dir_name=None, filename='default.json'):
        if request.user.is_superuser:
            sysout = sys.stdout

            if dir_name is None:
                dir_name = dir_name_object(self)

            path = '{}/fixtures/{}'.format(dir_name, filename)
            sys.stdout = open(path, 'w')
            call_command('dumpdata', dir_name)
            sys.stdout = sysout
        else:
            messages.warning(request, "Не достаточно прав!")
    set_fixtures.short_description = 'Фикстуры:Сохранить'

    def load_fixtures(self, request, queryset, dir_name=None, filename='default.json'):
        if request.user.is_superuser:
            if dir_name is None:
                dir_name = dir_name_object(self)

            try:
                path = '{}/fixtures/{}'.format(dir_name, filename)
                call_command('loaddata', path, verbosity=0)
            except CommandError:
                messages.error(request, "Ошибка выполнения команды:(")
        else:
            messages.warning(request, "Не достаточно прав!")
    load_fixtures.short_description = 'Фикстуры:Загрузить'


class AbstractDefaultAdmin(admin.ModelAdmin, BaseAdmin):
    class Meta:
        abstract = True

    empty_value_display = '-'
    save_on_top = True
    actions = (CloneObjectMixin.action_name,)


# -------------------
# - DEFAULT MPTT -
# -------------------

class AbstractDefaultMPTTAdmin(MPTTModelAdmin, BaseAdmin):
    class Meta:
        abstract = True

    mptt_level_indent = 23
    search_fields = ('title', 'parent__title')
    actions = ('rebuild', CloneObjectMixin.action_name)
    list_filter = ('parent',)

    def rebuild(self, request, queryset):
        self.model.objects.rebuild()
    rebuild.short_description = 'Пересобрать пункты раздела'

    def save_model(self, request, obj, form, change):
        try:
            super(AbstractDefaultMPTTAdmin, self).save_model(request, obj, form, change)
        except AttributeError:
            self.model.objects.rebuild()


# -------------------
# - DEFAULT INLINE -
# -------------------

class BaseInlineAdmin:
    extra = 0
    show_change_link = True


class AbstractDefaultStackedInlineAdmin(BaseInlineAdmin, admin.StackedInline):
    pass


class AbstractDefaultTabularInlineAdmin(BaseInlineAdmin, admin.TabularInline):
    pass
