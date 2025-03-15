from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import first

from goods.models import Categories



def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
        'categories':categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о там какие мы крутые прогеры)))))))))'
    }
    return render(request, 'main/about.html', context)