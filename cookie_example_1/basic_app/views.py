from django.shortcuts import render

# Create your views here.

def count_view(request):
    count = int(request.COOKIES.get('count',0))
    new_count = count+1
    context = {'count':new_count}
    response = render(request,"basic_app/count.html",context)
    response.set_cookie('count',new_count,max_age=30)
    return response
