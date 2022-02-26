from django.contrib import admin
from .models import Product,Slider,Navbar


class AdminProduct(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Product,AdminProduct)
admin.site.register(Slider)
admin.site.register(Navbar)