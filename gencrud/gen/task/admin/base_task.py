from django.contrib import admin
from gen.abstract.admin import AbstractMPTTPageSeoAdmin, AbstractImageInlineAdmin, fields_element
from task.models.task import Task
from task.models.task_image import TaskImage


class TaskImageInline(AbstractImageInlineAdmin):
    model = TaskImage


@admin.register(Task)
class BaseTaskAdmin(AbstractMPTTPageSeoAdmin):
    inlines = (TaskImageInline,)

    fieldsets = (
        fields_element(('parent',)),
        AbstractMPTTPageSeoAdmin.fieldsets[0],
        AbstractMPTTPageSeoAdmin.fieldsets[2],
        AbstractMPTTPageSeoAdmin.fieldsets[3],
    )
