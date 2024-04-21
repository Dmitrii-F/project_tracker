from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        projects_list_url = reverse('tasks:projects_list')
        html = (f"<h1>Страница приложения tasks</h1>"
                f"<a href='{projects_list_url}'>Список проектов</a>"
                f"<br/><br/><br/><a href='/control'>Контроль качества</a>")
        return HttpResponse(html)

class ProjectsListView(ListView):
    model = Project

    def get(self, request, *args, **kwargs):
        projects = self.get_queryset()
        projects_html = '<h1>Список проектов</h1><ul>'
        for project in projects:
            projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
        projects_html += '</ul>'
        return HttpResponse(projects_html)

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        project = self.object
        tasks = project.tasks.all()
        response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
        response_html += '<h2>Задачи</h2><ul>'
        for task in tasks:
            response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
        response_html += '</ul>'
        return HttpResponse(response_html)

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
        return HttpResponse(response_html)
