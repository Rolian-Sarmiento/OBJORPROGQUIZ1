from django.shortcuts import render
from.settings import DEBUG

def tab(request):
    return render(request, "home.html")

def tab1(request):
    return render(request, "about.html")
