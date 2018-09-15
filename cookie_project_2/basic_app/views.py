from django.shortcuts import render

# Create your views here.

def name_view(request):
    context={}
    return render(request,"basic_app/name.html",context)

def age_view(request):
    name = request.GET['name']
    response = render(request,"basic_app/age.html")
    response.set_cookie('name',name)
    return(response) 
