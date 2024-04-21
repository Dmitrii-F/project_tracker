from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('control:bug_list')
        feature_list_url = reverse('control:feature_list')
        html = (f"<h1>Система контроля качества</h1>"
                f"<a href='{bug_list_url}'>Список всех багов</a>"
                f"<br/><a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)

class BugListView(ListView):
    model = BugReport
    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a><a>...{bug.status}</a></li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)

class FeatureListView(ListView):
    model = FeatureRequest
    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1><ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a><a>...{feature.status}</a></li>'
        features_html += '</ul>'
        return HttpResponse(features_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        bug_html = (f'<h1>{bug.title}</h1>'
                    f'<h3>{bug.description}</h3>'
                    f'<p>{bug.project}/ {bug.task}/</p>'
                    f'<p> {bug.status} ... priority: {bug.priority} </p>'
                    f'<p> {bug.created_at} ... {bug.updated_at}</p>')
        return HttpResponse(bug_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        feature_html = (f'<h1>{feature.title}</h1>'
                        f'<h3>{feature.description}</h3>'
                        f'<p>{feature.project}/ {feature.task}/</p>'
                        f'<p> {feature.status} ... priority: {feature.priority} </p>'
                        f'<p> {feature.created_at} ... {feature.updated_at}</p>')
        return HttpResponse(feature_html)
