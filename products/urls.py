from django.urls import path
from . import views

urlpatterns = [
    path('',views.Car),
    path('erfan/',views.erfan)
]