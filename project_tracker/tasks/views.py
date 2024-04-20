from django.http import HttpResponse
from django.urls import reverse

def index(request):
    another_page_url = reverse('tasks:another_page')
    html = (f"<h1>Страница приложения tasks</h1>"
            f"<a href='{another_page_url}'>Перейти на другую страницу</a>"
            f"<br/><br/><br/><a href='/control'>Контроль качества</a>")
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")