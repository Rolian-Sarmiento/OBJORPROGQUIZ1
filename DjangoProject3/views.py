from django.shortcuts import render
from.settings import DEBUG


def tab(request):
    return render(request, "home.html")

def tab1(request):
    return render(request, "about.html")

def list_view(request):
    return render(request, "list.html")
