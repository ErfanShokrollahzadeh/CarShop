# from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def Car(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def erfan(request):
    return render(request,'index1.html')
