from django.urls import path

from admins.views import index, UserCreateView, admin_users_update, admin_users_remove, UserListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    #path('users/', admin_users, name='admin_users'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:id>/', admin_users_remove, name='admin_users_remove'),
]