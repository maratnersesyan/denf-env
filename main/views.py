from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'HOME - Главная',
        'content': 'Главная страница магазина - HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'HOME - Главная',
        'content': 'О нас',
        'text_on_page': '"Замечательный магазин! Всегда нахожу здесь то, что нужно. Вежливые и грамотные консультанты, которые всегда помогут с выбором. Очень радует широкий ассортимент и быстрая доставка. Спасибо за вашу работу!"'
    }
    return render(request, 'main/about.html', context)
