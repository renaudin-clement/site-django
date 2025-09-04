from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "myApp/home.html",     )

def start(request):
    return HttpResponse("<p> Hello, world. You're at the polls index.</p> ")

def error(request):
    return render(request, "myApp/error.html",     )
