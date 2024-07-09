from django.http import HttpResponse
from django.shortcuts import render  # Добавлен импорт функции render

def index_view(request):
    data = {
        'caption': "KatanaClub"
    }
    return render(request, 'myapp/index.html', data)

def art_view(request):
    return render(request, 'myapp/new_index.html')

def training_view(request):
    return render(request, 'myapp/training.html')

def events_view(request):
    return render(request, 'myapp/events.html')