from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project

# Create your views here.
from django.http import HttpResponse

from .models import Project

def index(request):

    #Counting visit using session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    num_projects = Project.objects.all().count()

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'num_projects': num_projects, 'num_visits': num_visits, 'form': form}

    return render(request, 'index.html', context=context)

@login_required
def create(request):

    form = ProjectForm(request.POST or None)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.instance.creator = request.user
    #         form.save()
            #return HttpResponseRedirect("/") 
    if form.is_valid():
        form.instance.creator = request.user
        form.save()
        return HttpResponseRedirect("/projects/projects")
    context = {"form":form}

    return render(request, 'project_form.html', context)

from django.views import generic

@login_required
def update(request, id):

    context = {}
    obj = get_object_or_404(Project, id = id)
    form = ProjectForm(request.POST or None, instance = obj)

    if form.is_valid():
        #form.instance.creator = request.user
        form.save()
        return HttpResponseRedirect("/projects/projects")
    context["form"] = form

    return render(request, 'project_update_form.html', context)


class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return (
            Project.objects.filter(creator=self.request.user).order_by('created_at')
        )