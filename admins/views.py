from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'Geekshop - Админ Панель'}
    return render(request, 'admins/index.html', context)

# create
def admin_users_create(request):
    context = {'title': 'Geekshop - Создание пользователя'}
    return render(request, 'admins/admin-users-create.html', context)

# read
def admin_users(request):
    context = {'title': 'Geekshop - Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)

#ubdate
def admin_users_update(request):
    context = {'title': 'Geekshop - Обнавление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)

#delete
def admin_users_delete(request):
    pass