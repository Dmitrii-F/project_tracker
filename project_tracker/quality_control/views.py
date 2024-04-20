from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_list_url = reverse('control:bug_list')
    feature_list_url = reverse('control:feature_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bug_list_url}'>Список всех багов</a>"
            f"<br/><a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
