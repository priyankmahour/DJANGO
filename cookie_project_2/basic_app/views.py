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


def job_view(request):
    age = request.GET['age']
    response = render(request,"basic_app/job.html")
    response.set_cookie('age',age)
    return(response)


def result_view(request):
    job =  request.GET['job']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    context ={'name':name,'job':job,'age':age}
    response = render(request,"basic_app/result.html",context)
    return(response)
