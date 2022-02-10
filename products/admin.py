from django.contrib import admin

# Register your models here.

from products.models import ProductCategory, Product
from baskets.models import Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description',('price','quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-name',)
    search_fields = ('name',)

