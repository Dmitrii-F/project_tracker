from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404

def index(request):
    bug_list_url = reverse('control:bug_list')
    feature_list_url = reverse('control:feature_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bug_list_url}'>Список всех багов</a>"
            f"<br/><a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a><a>...{bug.status}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a><a>...{feature.status}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    bug_html = (f'<h1>{bug.title}</h1>'
                f'<h3>{bug.description}</h3>'
                f'<p>{bug.project}/ {bug.task}/</p>'
                f'<p> {bug.status} ... priority: {bug.priority} </p>'
                f'<p> {bug.created_at} ... {bug.updated_at}</p>')
    return HttpResponse(bug_html)

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    feature_html = (f'<h1>{feature.title}</h1>'
                    f'<h3>{feature.description}</h3>'
                    f'<p>{feature.project}/ {feature.task}/</p>'
                    f'<p> {feature.status} ... priority: {feature.priority} </p>'
                    f'<p> {feature.created_at} ... {feature.updated_at}</p>')
    return HttpResponse(feature_html)