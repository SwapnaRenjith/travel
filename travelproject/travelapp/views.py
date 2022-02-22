from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj2})







# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("hello am contact")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})

