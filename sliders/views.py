from django.shortcuts import render
from .models import Slider, Slider2


def slid(request):
    sliders = Slider.objects.all()
    return render(request,'index.html',{'sliders':sliders})

def slid2(request):
    Slider2 = Slider2.objects.all()
    return render(request,'index.html',{'slider2':slider2})