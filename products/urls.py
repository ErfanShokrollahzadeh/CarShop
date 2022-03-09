from django.urls import path
from . import views

urlpatterns = [
    path('',views.Car),
    path('BMW/',views.BMW),
    path('BENZ/',views.BENZ),
    path('Ferrari/',views.Ferrari),
    path('Lamborghini/',views.Lamborghini),
    path('Bugatti/',views.Bugatti),
    path('maclaren/',views.maclaren),
    path('pagani/',views.pagani),
    path('toyota/',views.toyota),
    path('Confirmed/',views.Confirmed)
]