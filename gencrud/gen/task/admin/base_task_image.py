from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from task.models.task_image import TaskImage
from gen.task.strings import NAME_APP as TASK_NAME_APP


@admin.register(TaskImage)
class BaseTaskImageAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    raw_id_fields = (TASK_NAME_APP,)
    list_filter = (TASK_NAME_APP,) + AbstractImageAdmin.list_filter
    list_display = (TASK_NAME_APP,) + AbstractImageAdmin.list_display
