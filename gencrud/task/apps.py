from django.apps import AppConfig
from gen.task.strings import BASE_TASK_VERBOSE_NAME, NAME_APP


class TaskConfig(AppConfig):
    name = NAME_APP
    verbose_name = BASE_TASK_VERBOSE_NAME
