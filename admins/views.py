from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm
from django.urls import reverse

# Create your views here.

def index(request):
    context = {'title': 'Geekshop - Админ Панель'}
    return render(request, 'admins/index.html', context)

# create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
          #  messages.success(request, "Вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Geekshop - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)

# read
def admin_users(request):
    context = {'title': 'Geekshop - Пользователи',
               'users': User.objects.all(),
               }
    return render(request, 'admins/admin-users-read.html', context)

#ubdate
def admin_users_update(request):
    context = {'title': 'Geekshop - Обнавление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)

#delete
def admin_users_delete(request):
    pass