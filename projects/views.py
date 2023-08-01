from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm

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

from django.views import generic


class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreateView(generic.CreateView):
    model = Project

    fields = ['title', 'reb_num', 'participant_expected_num', 'expected_start_date']
    form = ProjectForm()

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(ProjectCreateView, self).form_valid(form)

class ProjectUpdateView(generic.UpdateView):
    model = Project

    fields = ['title', 'reb_num', 'participant_expected_num', 'expected_start_date']

class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return (
            Project.objects.filter(creator=self.request.user).order_by('created_at')
        )