# from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Slider

def Car(request):
    products = Product.objects.all()
    sliders = Slider.objects.all()
    return render(request,'index.html',{'products':products,'sliders':sliders})


def erfan(request):
    return render(request,'index1.html')
