from django.contrib import admin
from .models import Product


class AdminProduct(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Product,AdminProduct)