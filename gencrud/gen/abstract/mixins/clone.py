from django.contrib import messages
from django.utils.html import mark_safe
from gen.utils.todo import create_bug_issue


class CloneObjectMixin:
    action_name = 'clone_object'
    short_description = 'Клонировать'
    prefix_clone = '_CLONE'

    def __init__(self, clone=None):
        self.clone = clone

    @classmethod
    def clone_success(cls, request, obj):
        title = 'Объект клонирован! <b>{}</b>'.format(obj)
        messages.success(request, mark_safe(title))

    @classmethod
    def clone_error(cls, request, obj):
        title = 'Сбой клонирования! <b>{}</b>'.format(obj)
        messages.warning(request, mark_safe(title))
        create_bug_issue(title)

    @classmethod
    def is_valid(cls, obj):
        return (
                hasattr(obj, 'title') or hasattr(obj, 'image_title') or hasattr(obj, 'email') or hasattr(obj, 'name')
        )

    def clone_queryset(self, request, queryset):
        [self._clone_object(request, obj) for obj in queryset]

    def clone_format(self, value):
        return '{}{}'.format(value, self.prefix_clone) if value else self.prefix_clone

    def _clone_object(self, request, obj):
        if self.is_valid(obj):
            clone = self._prepare(obj)
            clone.save()
            self.clone_success(request, obj)
        else:
            self.clone_error(request, obj)

    def _prepare(self, obj):
        clone = obj
        clone.id = None

        self._set_clone_model_seo_page(clone)
        self._set_clone_model_image(clone)
        self._set_clone_model_user(clone)
        self._set_clone_product_item(clone)

        return self.clone

    def _set_clone_model_seo_page(self, clone):
        if hasattr(clone, 'title') and hasattr(clone, 'slug'):
            clone.title = self.clone_format(clone.title)
            clone.description = self.clone_format(clone.description)
            clone.slug = self.clone_format(clone.slug)
            clone.seo_title = self.clone_format(clone.seo_title)
            clone.seo_description = self.clone_format(clone.seo_description)
            clone.seo_keywords = self.clone_format(clone.seo_keywords)
            clone.sort = -1
            self.clone = clone

    def _set_clone_model_image(self, clone):
        if hasattr(clone, 'image_title') and not hasattr(clone, 'slug'):
            clone.image_title = self.clone_format(clone.image_title)
            clone.image_description = self.clone_format(clone.image_description)
            self.clone = clone

    def _set_clone_model_user(self, clone):
        if hasattr(clone, 'email'):
            clone.email = self.clone_format(clone.email)
            clone.username = self.clone_format(clone.username)
            clone.first_name = self.clone_format(clone.first_name)
            clone.last_name = self.clone_format(clone.last_name)
            clone.is_superuser = clone.is_active = False
            self.clone = clone

    def _set_clone_product_item(self, clone):
        if hasattr(clone, 'name'):
            clone.name = self.clone_format(clone.name)
            self.clone = clone

    def _set_clone_default(self, clone):
        if hasattr(clone, 'title') and not hasattr(clone, 'slug'):
            clone.title = self.clone_format(clone.title)
        if hasattr(clone, 'sort'):
            clone.sort = -1
        self.clone = clone
