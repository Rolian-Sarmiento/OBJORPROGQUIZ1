from django.shortcuts import render
from .models import Project

def listview(request):
    qs = Project.objects.all()
    print(qs)
    context = {'qsVar':qs}
    return render(request, 'list.html', context)
