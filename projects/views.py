from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Project

def index(request):
    ##return HttpResponse("Hello, world. You're at the projects index.")
    num_projects = Project.objects.all().count()

    context = {'num_projects': num_projects}

    return render(request, 'index.html', context=context)

from django.views import generic

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DeleteView):
    model = Project