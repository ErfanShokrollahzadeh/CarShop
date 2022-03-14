from django.contrib import admin
from .models import Product, Slider, Navbar, Footer, Slider2, LastestNew


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, AdminProduct)
admin.site.register(Slider)
admin.site.register(Navbar)
admin.site.register(Footer)
admin.site.register(Slider2)
admin.site.register(LastestNew)
