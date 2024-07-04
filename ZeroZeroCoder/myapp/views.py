from django.http import HttpResponse
from django.shortcuts import render  # Добавлен импорт функции render

def index_view(request):
    return render(request, 'myapp/index.html')

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Это страница для данных Data</p>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Это страница для тестов Test</p>")

