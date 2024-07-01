from django.http import HttpResponse

def index_view(request):
    return HttpResponse("<h1>Главная страница</h1><p>Это главная страница</p>")

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Это страница для данных Data</p>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Это страница для тестов Test</p>")
