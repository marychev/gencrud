from django.urls import path
from task.views.task_detail import TaskDetailView
from gen.task.strings import NAME_APP

urlpatterns = [
    path(r'<str:slug>/', TaskDetailView.as_view(), name=NAME_APP),
]
