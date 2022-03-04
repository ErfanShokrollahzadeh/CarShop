# from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Slider,Footer,Navbar

def Car(request):
    products = Product.objects.all()
    sliders = Slider.objects.all()
    footers = Footer.objects.all()
    navbars = Navbar.objects.all()
    return render(request,'index.html',{'products':products,'sliders':sliders,'footers':footers,'navbars':navbars})


def erfan(request):
    return render(request,'index1.html')