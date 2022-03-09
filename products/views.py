# from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Slider,Footer,Navbar,Slider2

def Car(request):
    products = Product.objects.all()
    sliders = Slider.objects.all()
    footers = Footer.objects.all()
    navbars = Navbar.objects.all()
    Sliders2 = Slider2.objects.all()
    return render(request,'index.html',{'products':products,'sliders':sliders,'footers':footers,'navbars':navbars,'Sliders2':Sliders2})


def BMW(request):
    sliders = Slider.objects.all()
    return render(request,'index2.html',{'sliders':sliders})

def BENZ(request):
    sliders = Slider.objects.all()
    return render(request,'index3.html',{'sliders':sliders})

def Ferrari(request):
    sliders = Slider.objects.all()
    return render(request,'index4.html',{'sliders':sliders})

def Lamborghini(request):
    sliders = Slider.objects.all()
    return render(request,'index5.html',{'sliders':sliders})

def Bugatti(request):
    sliders = Slider.objects.all()
    return render(request,'index6.html',{'sliders':sliders})

def maclaren(request):
    sliders = Slider.objects.all()
    return render(request,'index7.html',{'sliders':sliders})

def pagani (request):
    sliders = Slider.objects.all()
    return render(request,'index8.html',{'sliders':sliders})

def toyota(request):
    sliders = Slider.objects.all()
    return render(request,'index9.html',{'sliders':sliders})

def Confirmed(request):
    return render(request,'confirmed.html')
