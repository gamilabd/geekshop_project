from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView


# Create your views here.


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Geekshop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# create


@user_passes_test(lambda u: u.is_staff)
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


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {'title': 'Geekshop - Пользователи',
#                'users': User.objects.all(),
#                }
#     return render(request, 'admins/admin-users-read.html', context)


# ubdate
@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == "POST":
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Geekshop - Обнавление пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete
@user_passes_test(lambda u: u.is_staff)
def admin_users_remove(request, id):
    user = User.objects.get(id=id)
    # user.safe_delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
