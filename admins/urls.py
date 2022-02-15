from django.urls import path

from admins.views import index, UserCreateView, UserUpdateView, UserDeleteView, UserListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    #path('users/', admin_users, name='admin_users'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
]