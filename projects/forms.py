from django.forms import ModelForm

from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'reb_num', 'creator']