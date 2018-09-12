from django.shortcuts import render

# Create your views here.
from .models import *

def upper_view(request):
    data=Company.objects.all()
    context = {"data":data}
    return render(request,"basic_App/upper.html",context)


def truncate_view(request):
    data=Company.objects.all()
    context = {"data":data}
    return render(request,"basic_App/truncate.html",context)
