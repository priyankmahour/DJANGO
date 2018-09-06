from django.shortcuts import render

# Create your views here.
from . import forms

def index_view(request):
    context ={}
    return render(request,"basic_app/index.html",context)

def register_view(request):
    form = forms.StudentRegister()
    context = {"form":form}
    if request.method=="POST":
        form=forms.StudentRegister(data=request.POST)
        if form.is_valid():
            print("Form Validation Success  !!!")
            form.save(commit=True)
            print("Form saved to Database !!!  ")
            return index_view(request)
        else:
            print("Form Invalid")

    return render(request,"basic_app/register.html",context)
