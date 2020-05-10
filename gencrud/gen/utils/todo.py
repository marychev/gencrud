def create_bug_issue(error_title):
    from task.models.task import Task
    task, _ = Task.objects.get_or_create(title=error_title)

