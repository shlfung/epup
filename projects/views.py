from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Project

def index(request):

    #Counting visit using session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    num_projects = Project.objects.all().count()

    context = {'num_projects': num_projects, 'num_visits': num_visits}

    return render(request, 'index.html', context=context)

from django.views import generic


class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectListView(generic.ListView):
    model = Project
