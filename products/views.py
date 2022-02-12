
# Create your views here.

from django.shortcuts import render
import os
import json
from datetime import datetime
from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, Page

MODULE_DIR = os.path.dirname(__file__)  # в этой переменной будем сдержать путь до папки products


def index(request):
    context = {
        'title': 'GeekShop',
        'now_date': datetime.now(),
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1, pk=None):  #(request, category_id=None, pk=None)
    #print(pk)
    #file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')  # содержить польный путь до файла goods.json
    context = {'title': 'GeekShop-Каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    context['products'] = products
    return render(request, 'products/products.html', context)
