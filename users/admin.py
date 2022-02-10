from django.contrib import admin

# Register your models here.

from users.models import User
from baskets.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)
