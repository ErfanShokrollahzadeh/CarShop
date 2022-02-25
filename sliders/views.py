from django.shortcuts import render
from .models import Slider

def slid(request):
    sliders = Slider.objects.all()
    return render(request,'index.html',{'sliders':sliders})