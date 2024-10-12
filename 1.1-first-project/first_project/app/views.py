from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    templateName = 'app/home.html'
    
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    context = {
        'pages': pages
    }

    return render(request, templateName, context)


def time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
    message = f'Текущее время: {current_time}'

    return HttpResponse(message)


def workdir_view(request):
    current = os.listdir(os.getcwd())
    message = f'Содержимое рабочей директории: {current}'

    return HttpResponse(message)
