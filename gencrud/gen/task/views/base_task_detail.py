from django.views.generic.base import TemplateView
from gen.mixins import MainPageMixin
from gen.utils.pagination import get_pagination
from gen.utils.leftbar import get_leftbar
from task.models.task import Task
from task.models.task_image import TaskImage


class BaseTaskDetailView(MainPageMixin, TemplateView):
    template_name = 'task/templates/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(BaseTaskDetailView, self).get_context_data(**kwargs)

        context['object'] = Task.objects.get(slug=context['slug'])
        context['leftbar'] = get_leftbar(Task, context['object'])
        task_id = context['leftbar']['root_obj'].id
        context['current_mainmenu'] = context['mainmenu'].filter(
            task_id=task_id
        ).first()

        context['objects'] = TaskImage.objects.filter(task_id=context['object'])
        context['objects'] = get_pagination(self.request, context['objects'])

        return context
