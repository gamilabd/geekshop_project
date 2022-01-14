
# Create your views here.

from django.shortcuts import render
import os
import json

MODULE_DIR = os.path.dirname(__file__)  # в этой переменной будем сдержать путь до папки products


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, pk=None):
    print(pk)
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')  # содержить польный путь до файла goods.json
    context = {
        'title': 'GeekShop-Каталог',
        'link_menu': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'products': json.load(open(file_path, encoding="utf-8")),
    }
    return render(request, 'products/products.html', context)
