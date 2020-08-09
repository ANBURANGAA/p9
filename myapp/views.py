from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.

def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Ranga"
    return render(request,"myapp/profile.html",{'name':name})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h4>factorial is {}</h4>".format(factorial(n)))

def child(request):
    return render(request,"child.html")

def sample(request):
    return render(request,"myapp/sample.html")